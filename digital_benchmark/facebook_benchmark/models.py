from django.db import models
from django.contrib.auth.models import User

from enum import Enum

class SoftDeleteMixin(models.Model):
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class CreateUpdateMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True

class FacebookProfile(SoftDeleteMixin, CreateUpdateMixin):
    access_token = models.TextField(null=True, blank=False)
    expires_at = models.DateTimeField(null=True, blank=False)
    facebook_id = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, null=True, blank=False)
    last_name = models.CharField(max_length=255, null=True, blank=False)

    user = models.OneToOneField(User, related_name='facebook_profile', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Facebook Profile'
        verbose_name_plural = 'Facebook Profiles'

    def __str__(self):
        return f'{self.first_name} {self.last_name}' 

class Page(SoftDeleteMixin, CreateUpdateMixin):
    access_token = models.TextField(null=True, blank=False)
    displayed_message_response_time = models.CharField(max_length=255, null=True, blank=False)
    expires_at = models.DateTimeField(null=True, blank=False)
    fan_count = models.IntegerField(null=True, blank=False)
    name = models.CharField(max_length=255, null=True, blank=False)
    num_engagements = models.IntegerField('total engagements', null=True, blank=False)
    overall_star_rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=False)
    page_consumptions = models.IntegerField(null=True, blank=False)
    page_consumptions_unique = models.IntegerField(null=True, blank=False)
    page_engaged_users = models.IntegerField(null=True, blank=False)
    page_id = models.CharField(max_length=255)
    page_impressions = models.IntegerField(null=True, blank=False)
    page_impressions_nonviral = models.IntegerField(null=True, blank=False)
    page_impressions_nonviral_unique = models.IntegerField(null=True, blank=False)
    page_impressions_organic = models.IntegerField(null=True, blank=False)
    page_impressions_organic_unique = models.IntegerField(null=True, blank=False)
    page_impressions_paid = models.IntegerField(null=True, blank=False)
    page_impressions_paid_unique = models.IntegerField(null=True, blank=False)
    page_impressions_unique = models.IntegerField(null=True, blank=False)
    page_impressions_viral = models.IntegerField(null=True, blank=False)
    page_impressions_viral_unique = models.IntegerField(null=True, blank=False)
    page_negative_feedback = models.IntegerField(null=True, blank=False)
    page_negative_feedback_unique = models.IntegerField(null=True, blank=False)
    page_post_engagements = models.IntegerField(null=True, blank=False)
    page_video_views = models.IntegerField(null=True, blank=False)
    page_views_total = models.IntegerField(null=True, blank=False)
    rating_count = models.IntegerField(null=True, blank=False)
    talking_about_count = models.IntegerField(null=True, blank=False)
    unread_message_count = models.IntegerField(null=True, blank=False)
    unread_notif_count = models.IntegerField('unread notification count', null=True, blank=False)
    unseen_message_count = models.IntegerField(null=True, blank=False)
    verification_status = models.CharField(max_length=255, null=True, blank=False)

    facebook_profile = models.ForeignKey('facebook_benchmark.FacebookProfile', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class RecommendationChoice(Enum):
    NEGATIVE = 'NEGATIVE'
    NONE = 'NONE'
    POSITIVE = 'POSITIVE'

    @classmethod
    def get_recommendation_choices(cls):
        return [(recommendation.value, recommendation.value.title()) for recommendation in RecommendationChoice]

class Rating(SoftDeleteMixin, CreateUpdateMixin):
    created_time = models.DateTimeField()
    rating = models.SmallIntegerField(null=True, blank=True)
    recommendation_type = models.CharField(max_length=8, choices=RecommendationChoice.get_recommendation_choices())
    review_text = models.TextField(null=True, blank=True)

    page = models.ForeignKey('facebook_benchmark.Page', related_name='ratings', on_delete=models.PROTECT)

    def __str__(self):
        return self.review_text

class TimelineVisibilityChoice(Enum):
    HIDDEN = 'HIDDEN'
    NORMAL = 'NORMAL'
    FORCED_ALLOW = 'FORCED_ALLOW'
    NO_TIMELINE_UNIT_FOR_THIS_POST = "NO_TIMELINE_UNIT_FOR_THIS_POST"

    @classmethod
    def get_timeline_visibility_choices(cls):
        return [(timeline_visibility.value, timeline_visibility.value.replace('_', ' ').title()) for timeline_visibility in TimelineVisibilityChoice]

class Post(SoftDeleteMixin, CreateUpdateMixin):
    backdated_time = models.DateTimeField(null=True, blank=True)
    created_time = models.DateTimeField(null=True, blank=False)
    is_eligible_for_promotion = models.BooleanField(null=True, blank=False)
    is_expired = models.BooleanField(null=True, blank=False)
    is_hidden = models.BooleanField(null=True, blank=False)
    is_instagram_eligible = models.BooleanField(null=True, blank=False)
    is_popular = models.BooleanField(null=True, blank=False)
    is_published = models.BooleanField(null=True, blank=False)
    message = models.TextField(null=True, blank=True)
    post_clicks = models.IntegerField(null=True, blank=False)
    post_clicks_unique = models.IntegerField(null=True, blank=False)
    post_engaged_fan = models.IntegerField(null=True, blank=False)
    post_engaged_users = models.IntegerField(null=True, blank=False)
    post_id = models.CharField(max_length=255, null=True, blank=False)
    post_impressions = models.IntegerField(null=True, blank=False)
    post_impressions_fan = models.IntegerField(null=True, blank=False)
    post_impressions_fan_paid = models.IntegerField(null=True, blank=False)
    post_impressions_fan_paid_unique = models.IntegerField(null=True, blank=False)
    post_impressions_fan_unique = models.IntegerField(null=True, blank=False)
    post_impressions_nonviral = models.IntegerField(null=True, blank=False)
    post_impressions_nonviral_unique = models.IntegerField(null=True, blank=False)
    post_impressions_organic = models.IntegerField(null=True, blank=False)
    post_impressions_organic_unique = models.IntegerField(null=True, blank=False)
    post_impressions_paid = models.IntegerField(null=True, blank=False)
    post_impressions_unique = models.IntegerField(null=True, blank=False)
    post_impressions_viral = models.IntegerField(null=True, blank=False)
    post_impressions_viral_unique = models.IntegerField(null=True, blank=False)
    post_negative_feedback = models.IntegerField(null=True, blank=False)
    post_negative_feedback_unique = models.IntegerField(null=True, blank=False)
    post_reactions_anger_total = models.IntegerField(default=0, null=True, blank=False)
    post_reactions_haha_total = models.IntegerField(default=0, null=True, blank=False)
    post_reactions_like_total = models.IntegerField(default=0, null=True, blank=False)
    post_reactions_love_total = models.IntegerField(default=0, null=True, blank=False)
    post_reactions_sorry_total = models.IntegerField(default=0, null=True, blank=False)
    post_reactions_wow_total = models.IntegerField(default=0, null=True, blank=False)
    promotion_status = models.CharField(max_length=255, null=True, blank=False)
    scheduled_publish_time = models.DateTimeField(null=True, blank=True)
    shares = models.IntegerField(null=True, blank=False)
    story = models.TextField(null=True, blank=True)
    timeline_visibility = models.CharField(max_length=30, choices=TimelineVisibilityChoice.get_timeline_visibility_choices(), null=True, blank=False)
    updated_time = models.DateTimeField(null=True, blank=False)

    page = models.ForeignKey('facebook_benchmark.Page', on_delete=models.PROTECT)

    def __str__(self):
        return self.message or self.story or self.post_id

class Comment(SoftDeleteMixin, CreateUpdateMixin):
    comment_id = models.CharField(max_length=255)
    created_time = models.DateTimeField()
    from_id = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField()
    angry_total = models.IntegerField(default=0, null=True, blank=False)
    haha_total = models.IntegerField(default=0, null=True, blank=False)
    like_total = models.IntegerField(default=0, null=True, blank=False)
    love_total = models.IntegerField(default=0, null=True, blank=False)
    sad_total = models.IntegerField(default=0, null=True, blank=False)
    wow_total = models.IntegerField(default=0, null=True, blank=False)

    post = models.ForeignKey('facebook_benchmark.Post', related_name='comments', on_delete=models.PROTECT)

    def __str__(self):
        return self.message