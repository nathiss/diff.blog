"""
Django settings for diffblog project.

Generated by 'django-admin startproject' using Django 2.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from diffblog.secrets import (
    social_auth_github_key,
    social_auth_github_secret,
    postgresql_user,
    postgresql_password,
    smtp_hostname,
    smtp_username,
    smtp_password,
    smtp_port,
    django_secret,
)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SITE_BASE_URL = "https://diff.blog"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = django_secret

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
DEVELOPMENT = False

ALLOWED_HOSTS = ["diff.blog", "www.diff.blog"]
CORS_ORIGIN_WHITELIST = [
    "http://localhost:8080",
    "https://diff.blog",
    "https://vishnuks.com",
]

STATICFILES_DIRS = []

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    "django.contrib.postgres",
    "feed",
    "app",
    "jobs",
    "mirrors",
    "social_django",
    "django_rq",
    "corsheaders",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# After making change update /etc/supervisor/conf.d/rqueue.conf and restart the
# process
RQ_QUEUES = {
    "following_bootstrapper": {
        "HOST": "localhost",
        "PORT": 6379,
        "DB": 0,
    },
    "followers_bootstrapper": {
        "HOST": "localhost",
        "PORT": 6379,
        "DB": 0,
    },
    "feed": {
        "HOST": "localhost",
        "PORT": 6379,
        "DB": 0,
    },
    "language_scanner": {
        "HOST": "localhost",
        "PORT": 6379,
        "DB": 0,
    },
    "follow_organizations": {
        "HOST": "localhost",
        "PORT": 6379,
        "DB": 0,
    },
    "event_log_processor": {
        "HOST": "localhost",
        "PORT": 6379,
        "DB": 0,
    },
    "set_plugin_post_info": {
        "HOST": "localhost",
        "PORT": 6379,
        "DB": 0,
    },
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
        "KEY_PREFIX": "app_cache",
    }
}

CACHE_TTL = 60 * 1
SESSION_COOKIE_AGE = 60 * 60 * 24 * 365

ROOT_URLCONF = "diffblog.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
            ],
        },
    },
]

WSGI_APPLICATION = "diffblog.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "diffblog",
        "USER": postgresql_user,
        "PASSWORD": postgresql_password,
        "HOST": "127.0.0.1",
        "PORT": "",
    }
}

AUTHENTICATION_BACKENDS = ("social_core.backends.github.GithubOAuth2",)


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

SOCIAL_AUTH_PIPELINE = (
    # Get the information we can about the user and return it in a simple
    # format to create the user instance later. On some cases the details are
    # already part of the auth response from the provider, but sometimes this
    # could hit a provider API.
    "social_core.pipeline.social_auth.social_details",
    # Get the social uid from whichever service we're authing thru. The uid is
    # the unique identifier of the given user in the provider.
    "social_core.pipeline.social_auth.social_uid",
    # Verifies that the current auth process is valid within the current
    # project, this is where emails and domains whitelists are applied (if
    # defined).
    "social_core.pipeline.social_auth.auth_allowed",
    # Checks if the current social-account is already associated in the site.
    "social_core.pipeline.social_auth.social_user",
    # Make up a username for this person, appends a random string at the end if
    # there's any collision.
    "social_core.pipeline.user.get_username",
    # Send a validation email to the user to verify its email address.
    # Disabled by default.
    # 'social_core.pipeline.mail.mail_validation',
    # Associates the current social details with another user account with
    # a similar email address. Disabled by default.
    # 'social_core.pipeline.social_auth.associate_by_email',
    # Create a user account if we haven't found one yet.
    "social_core.pipeline.user.create_user",
    # Create the record that associates the social account with the user.
    "social_core.pipeline.social_auth.associate_user",
    # Populate the extra_data field in the social record with the values
    # specified by settings (and the default ones like access_token, etc).
    "social_core.pipeline.social_auth.load_extra_data",
    # Update the user record with any changed info from the auth service.
    "social_core.pipeline.user.user_details",
    "app.auth.get_github_info",
)

SOCIAL_AUTH_NEW_USER_REDIRECT_URL = "/signup/topics"
SOCIAL_AUTH_LOGIN_REDIRECT_URL = "/"
LOGIN_URL = "/"
SOCIAL_AUTH_GITHUB_SCOPE = ["user:email"]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "standard": {
            "format": "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            "datefmt": "%d/%b/%Y %H:%M:%S",
        },
    },
    "handlers": {
        "logfile": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "/home/vishnu/diff.blog/var/log/django.log",
            "maxBytes": 50000,
            "backupCount": 2,
            "formatter": "standard",
        },
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "propagate": True,
            "level": "WARN",
        },
        "django.db.backends": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False,
        },
        "app": {
            "handlers": ["console", "logfile"],
            "level": "DEBUG",
        },
        "feed": {
            "handlers": ["console", "logfile"],
            "level": "DEBUG",
        },
    },
}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

SOCIAL_AUTH_GITHUB_KEY = social_auth_github_key
SOCIAL_AUTH_GITHUB_SECRET = social_auth_github_secret
USE_TZ = True

EMAIL_USE_TLS = True
EMAIL_HOST = smtp_hostname
EMAIL_PORT = smtp_port
EMAIL_HOST_USER = smtp_username
EMAIL_HOST_PASSWORD = smtp_password
DEFAULT_FROM_EMAIL = "diff.blog <noreply@ses.diff.blog>"
