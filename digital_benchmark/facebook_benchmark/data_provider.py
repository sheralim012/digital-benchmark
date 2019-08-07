import facebook as fb
import requests

from django.conf import settings

class FacebookUserDataProvider:
    def __init__(self, user_access_token, *args, **kwargs):
        self.user_access_token = user_access_token
        self.graph_api_client = fb.GraphAPI(access_token=user_access_token, version=settings.FACEBOOK_GRAPH_API_VERSION)
    
    def get_profile(self, fields='', *args, **kwargs):
        fields = fields or ','.join(settings.FACEBOOK_DEFAULT_FIELDS_FOR_PROFILE)
        profile = self.graph_api_client.get_object(id='me', fields=fields)
        return profile
    
    def get_all_pages(self, fields='', *args, **kwargs):
        fields = fields or ','.join(settings.FACEBOOK_DEFAULT_FIELDS_FOR_ACCOUNTS)
        all_pages = self.graph_api_client.get_connections(id='me', connection_name='accounts', fields=fields)
        return all_pages

class FacebookPageDataProvider:
    def __init__(self, page_access_token, *args, **kwargs):
        self.page_access_token = page_access_token
        self.graph_api_client = fb.GraphAPI(access_token=page_access_token, version=settings.FACEBOOK_GRAPH_API_VERSION)
    
    def _get_next(self, next_url):
        return requests.get(next_url).json()

    def _append_ratings(self, page):
        ratings = page['ratings']
        while 'paging' in ratings and 'next' in ratings['paging']:
            ratings = self._get_next(ratings['paging']['next'])
            page['ratings']['data'] += ratings['data']

    def get_page_details(self, fields=''):
        page_fields = fields or ','.join(settings.FACEBOOK_DEFAULT_FIELDS_FOR_PAGE)
        page = self.graph_api_client.get_object(id='me', fields=page_fields)
        if 'ratings' in page:
            self._append_ratings(page)
        return page
    
    def _append_reactions(self, append_reactions_to):
        reactions = append_reactions_to['reactions']
        while 'paging' in reactions and 'next' in reactions['paging']:
            reactions = self._get_next(reactions['paging']['next'])
            append_reactions_to['reactions']['data'] += reactions['data']
    
    def _append_comments(self, post):
        all_comments = []
        comments = post['comments']
        while 'paging' in comments:
            for comment in comments['data']:
                if 'reactions' in comment:
                    self._append_reactions(comment)
                all_comments.append(comment)
            if not ('next' in comments['paging']):
                break
            comments = self._get_next(comments['paging']['next'])
        post['comments']['data'] = all_comments

    def get_all_posts_details(self, fields=''):
        posts_fields = fields or ','.join(settings.FACEBOOK_DEFAULT_FIELDS_FOR_FEED)
        feed = self.graph_api_client.get_connections(id='me', connection_name='feed', fields=posts_fields)
        all_posts = []
        while 'paging' in feed:
            for post in feed['data']:
                if 'reactions' in post:
                    self._append_reactions(post)
                if 'comments' in post:
                    self._append_comments(post)
                all_posts.append(post)
            if not ('next' in feed['paging']):
                break
            feed = self._get_next(feed['paging']['next'])
        return all_posts
    
    def get_post_details(self, post_id, fields=''):
        post_fields = fields or ','.join(settings.FACEBOOK_DEFAULT_FIELDS_FOR_POST)
        post = self.graph_api_client.get_object(id=post_id, fields=post_fields)
        if 'reactions' in post:
            self._append_reactions(post)
        if 'comments' in post:
            self._append_comments(post)
        return post
    
    def get_page_insights(self, metrices=''):
        page_metrices = metrices or ','.join(settings.FACEBOOK_DEFAULT_METRICES_FOR_PAGE_INSIGHTS)
        page_insights = self.graph_api_client.get_connections(id='me', connection_name='insights', metric=page_metrices, date_preset=settings.FACEBOOK_DEFAULT_DATE_PRESET_FOR_PAGE_INSIGHTS, period=settings.FACEBOOK_DEFAULT_PERIOD_FOR_PAGE_INSIGHTS)
        return page_insights
    
    def get_post_insights(self, post_id, metrices=''):
        post_metrices = metrices or ','.join(settings.FACEBOOK_DEFAULT_METRICES_FOR_POST_INSIGHTS)
        post_insights = self.graph_api_client.get_connections(id=post_id, connection_name='insights', metric=post_metrices)
        return post_insights
    
    def get_all_posts(self, fields='', metrices=''):
        all_posts_response = self.get_all_posts_details(fields)
        for post_details_response in all_posts_response:
            post_insights_response = self.get_post_insights(post_details_response['id'], metrices)
            post_details_response['insights'] = post_insights_response
        return all_posts_response