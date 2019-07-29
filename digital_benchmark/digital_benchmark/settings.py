"""
Django settings for digital_benchmark project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

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
    'facebook_benchmark', #register facebook_benchmark app
    'debug_toolbar', # register django-debug-toolbar
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
]

ROOT_URLCONF = 'digital_benchmark.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'digital_benchmark',
        'USER': 'digital_benchmark',
        'PASSWORD': 'digital_benchmark',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}


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
FACEBOOK_DEFAULT_FIELDS_FOR_PAGE = ['id', 'displayed_message_response_time', 'engagement', 'fan_count', 'name', 'overall_star_rating', 'rating_count', 'talking_about_count', 'unread_message_count', 'unread_notif_count', 'unseen_message_count', 'verification_status']
FACEBOOK_DEFAULT_FIELDS_FOR_FEED = ['id', 'backdated_time', 'created_time', 'is_eligible_for_promotion', 'is_hidden', 'is_popular', 'is_published', 'message', 'message_tags', 'promotion_status', 'scheduled_publish_time', 'shares', 'story', 'story_tags', 'timeline_visibility', 'updated_time', 'comments', 'likes', 'reactions', 'to']
FACEBOOK_DEFAULT_FIELDS_FOR_POST = ['id', 'backdated_time', 'created_time', 'is_eligible_for_promotion', 'is_hidden', 'is_popular', 'is_published', 'message', 'message_tags', 'promotion_status', 'scheduled_publish_time', 'shares', 'story', 'story_tags', 'timeline_visibility', 'updated_time', 'comments', 'likes', 'reactions', 'to']
FACEBOOK_DEFAULT_METRICES_FOR_PAGE_INSIGHTS = ['page_impressions', 'page_engaged_users', 'page_consumptions', 'page_negative_feedback', 'page_fans_online', 'page_actions_post_reactions_total', 'page_fans', 'page_fan_removes', 'page_views_total', 'page_video_views', 'page_posts_impressions']
FACEBOOK_DEFAULT_METRICES_FOR_POST_INSIGHTS = ['post_impressions', 'post_impressions_unique', 'post_impressions_fan', 'post_impressions_fan_unique', 'post_impressions_organic', 'post_impressions_organic_unique', 'post_impressions_viral', 'post_impressions_viral_unique', 'post_engaged_users', 'post_negative_feedback', 'post_negative_feedback_unique', 'post_engaged_fan', 'post_clicks', 'post_clicks_unique', 'post_reactions_by_type_total']

# for django-debug-toolbar
INTERNAL_IPS = [
    '127.0.0.1',
]