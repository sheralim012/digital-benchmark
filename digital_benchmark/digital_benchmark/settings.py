"""
Django settings for digital_benchmark project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from datetime import timedelta

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3-1jc^c3n(fw5sctlo*19&vh$-d6h7-45co-4_%totri3h9=^4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'twitter_benchmark', #register twitter_benchmark app
    'instagram_benchmark',
    'facebook_benchmark', # register facebook_benchmark app
    'accounts',
    'debug_toolbar', # register django-debug-toolbar
    'rest_framework', #register django rest framework
    'django_celery_results', #register django celery results
    'silk', #register django-silk
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware', # for django-debug-toolbar
    'silk.middleware.SilkyMiddleware', #for django-silk
]

ROOT_URLCONF = 'digital_benchmark.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'digital_benchmark.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=7),
}

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# facebook_benchmark settings
FACEBOOK_GRAPH_API_VERSION = '3.1'
FACEBOOK_APP_ID = '349831992602224'
FACEBOOK_APP_SECRET = 'e3bfa0ed905199eecca00e74631280b7'
FACEBOOK_APP_TOKEN = '349831992602224|uQIt8Jk7183kkz0-zT-jUf9uuAw'
FACEBOOK_LOGIN_SUCCESSFUL_REDIRECT_URI = 'http://localhost:8000/facebook_benchmark/login_successful'
FACEBOOK_SCOPE = ['manage_pages', 'pages_show_list', 'read_insights']
FACEBOOK_RESPONSE_TYPE = 'code'
FACEBOOK_STATE = '{"{st=state123abc,ds=123456789}"}'
FACEBOOK_LOGIN_URL = f"https://www.facebook.com/v{FACEBOOK_GRAPH_API_VERSION}/dialog/oauth?client_id={FACEBOOK_APP_ID}&redirect_uri={FACEBOOK_LOGIN_SUCCESSFUL_REDIRECT_URI}&scope={','.join(FACEBOOK_SCOPE)}&response_type={FACEBOOK_RESPONSE_TYPE}&state={FACEBOOK_STATE}"
FACEBOOK_ACCESS_TOKEN_URL = f"https://graph.facebook.com/v{FACEBOOK_GRAPH_API_VERSION}/oauth/access_token"
FACEBOOK_INSPECT_ACCESS_TOKEN_URL = f'https://graph.facebook.com/v{FACEBOOK_GRAPH_API_VERSION}/debug_token'
FACEBOOK_REREQUEST_SCOPE_URL = f"https://www.facebook.com/v{FACEBOOK_GRAPH_API_VERSION}/dialog/oauth?client_id={FACEBOOK_APP_ID}&redirect_uri={FACEBOOK_LOGIN_SUCCESSFUL_REDIRECT_URI}&auth_type=rerequest&scope={','.join(FACEBOOK_SCOPE)}"
FACEBOOK_PROFILE_DEFAULT_FIELDS = ['first_name', 'id', 'last_name']
FACEBOOK_ACCOUNTS_DEFAULT_FIELDS = ['access_token', 'id', 'name']
FACEBOOK_GRANT_TYPE = 'fb_exchange_token'
FACEBOOK_OBJECT_SELF = 'me'
FACEBOOK_CONNECTION_ACCOUNTS = 'accounts'
FACEBOOK_CONNECTION_RATINGS = 'ratings'
FACEBOOK_CONNECTION_POSTS = 'posts'
FACEBOOK_CONNECTION_REACTIONS = 'reactions'
FACEBOOK_CONNECTION_COMMENTS = 'comments'
FACEBOOK_PAGE_INSIGHTS_DEFAULT_DATE_PRESET = 'today'
FACEBOOK_PAGE_INSIGHTS_DEFAULT_PERIOD = 'days_28'
FACEBOOK_PAGE_INSIGHTS_DEFAULT_METRICES = ['page_consumptions', 'page_consumptions_unique', 'page_engaged_users', 'page_impressions', 'page_impressions_nonviral', 'page_impressions_nonviral_unique', 'page_impressions_organic', 'page_impressions_organic_unique', 'page_impressions_paid', 'page_impressions_paid_unique', 'page_impressions_unique', 'page_impressions_viral', 'page_impressions_viral_unique', 'page_negative_feedback', 'page_negative_feedback_unique', 'page_post_engagements', 'page_video_views', 'page_views_total']
FACEBOOK_PAGE_DEFAULT_FIELDS = ['displayed_message_response_time', 'engagement{count}', 'fan_count', 'id', 'name', 'overall_star_rating', 'rating_count', 'talking_about_count', 'unread_message_count', 'unread_notif_count', 'unseen_message_count', 'verification_status', f'insights.metric({",".join(FACEBOOK_PAGE_INSIGHTS_DEFAULT_METRICES)}).date_preset({FACEBOOK_PAGE_INSIGHTS_DEFAULT_DATE_PRESET}).period({FACEBOOK_PAGE_INSIGHTS_DEFAULT_PERIOD}){{name,values{{value}}}}']
FACEBOOK_PAGE_RATING_DEFAULT_FIELDS = ['created_time', 'review_text', 'rating', 'recommendation_type']
FACEBOOK_PAGE_POST_INSIGHTS_DEFAULT_METRICES = ['post_clicks', 'post_clicks_unique', 'post_engaged_fan', 'post_engaged_users', 'post_impressions', 'post_impressions_fan', 'post_impressions_fan_paid', 'post_impressions_fan_paid_unique', 'post_impressions_fan_unique', 'post_impressions_nonviral', 'post_impressions_nonviral_unique', 'post_impressions_organic', 'post_impressions_organic_unique', 'post_impressions_paid', 'post_impressions_paid_unique', 'post_impressions_unique', 'post_impressions_viral', 'post_impressions_viral_unique', 'post_negative_feedback', 'post_negative_feedback_unique', 'post_reactions_anger_total', 'post_reactions_haha_total', 'post_reactions_like_total', 'post_reactions_love_total', 'post_reactions_sorry_total', 'post_reactions_wow_total']
FACEBOOK_PAGE_POST_DEFAULT_FIELDS = ['backdated_time', 'created_time', 'id', 'is_eligible_for_promotion', 'is_expired','is_hidden', 'is_instagram_eligible', 'is_popular', 'is_published', 'message', 'promotion_status', 'scheduled_publish_time', 'shares', 'story', 'timeline_visibility', 'updated_time', f'insights.metric({",".join(FACEBOOK_PAGE_POST_INSIGHTS_DEFAULT_METRICES)}){{name, values{{value}}}}']
FACEBOOK_PAGE_POST_COMMENTS_DEFAULT_FIELDS = ['id', 'message', 'created_time', 'from{id}', 'reactions.type(ANGRY).limit(0).summary(total_count).as(angry),reactions.type(HAHA).limit(0).summary(total_count).as(haha),reactions.type(LIKE).limit(0).summary(total_count).as(like),reactions.type(LOVE).limit(0).summary(total_count).as(love),reactions.type(SAD).limit(0).summary(total_count).as(sad),reactions.type(WOW).limit(0).summary(total_count).as(wow)']



# twitter_benchmark setting
REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
BASE_AUTHORIZATION_URL = 'https://api.twitter.com/oauth/authorize'
PROFILE_DATA_URL = 'https://api.twitter.com/1.1/account/verify_credentials.json'
ACCESS_TOKEN_URL= 'https://api.twitter.com/oauth/access_token'
TWEETS_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
COMMENT_URL = 'https://api.twitter.com/1.1/statuses/mentions_timeline.json'
CONSUMER_KEY = 'LCE85J76ONueBmKn1SpVAjZ0F'
CONSUMER_SECRET = 'eo992TOAXA6n9KNrKy59Qkb8uKmTMRwE3XevUHeoFm3fXihbEJ'
TWEETS_COUNT = 200


# instagram settings and urls
PROFILE_URL="https://api.instagram.com/v1/users/self/?access_token={}"
RECENT_MEDIA_URL="https://api.instagram.com/v1/users/self/media/recent/?count=10&access_token={}"
COMMENTS_URL="https://api.instagram.com/v1/media/{}/comments?access_token={}"
INSTA_CONNECT_URL="https://api.instagram.com/oauth/authorize/?client_id=4d8f538893ba481f88c0614865dc9310&redirect_uri=http://127.0.0.1:8000/instagram_benchmark/connection_success&response_type=code&scope=basic"
CLIENT_ID='4d8f538893ba481f88c0614865dc9310'
CLIENT_SECRET='8e2bba68038844ab8e240b7094db18f2'
GRANT_TYPE='authorization_code'
INSTA_REDIRECT_URL='http://127.0.0.1:8000/instagram_benchmark/connection_success'
INSTA_FETCH_USER_URL='https://api.instagram.com/oauth/access_token'
#insta django internal configs
DJANGO_LOGIN_URL='http://127.0.0.1:8000/accounts/login/'
#Scrapyd Configs
SCRAPYD_SERVER_URL="http://127.0.0.1:6800/"
SCRAPER_AGENT='Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'

# for django-debug-toolbar
INTERNAL_IPS = [
    '127.0.0.1',
]

CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND = 'django-cache'

try:
  from .local_settings import *
except ImportError:
  pass
