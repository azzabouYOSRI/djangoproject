"""
Django settings for portfoliowebsite project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os


from django.conf import settings
from django.conf.global_settings import LOGIN_REDIRECT_URL
from django.contrib.auth import login
from django.contrib.auth.models import User

import base.forms

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-iaz4)-4_y9w(k+jb=v0viloa$ni6q+sqd6u6nb9*1lrv=f9czr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['portfolio-livestream.herokuapp.com',
                 '127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'base.apps.BaseConfig',
    'ckeditor',
    'ckeditor_uploader',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfoliowebsite.urls'

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

WSGI_APPLICATION = 'portfoliowebsite.wsgi.application'

ADMINS = (
     ('yosri azabou', 'college.yosri@gmail.com'),
)

MANAGERS = ADMINS

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'PORTFOLIO',
        'USER': 'postgres',
        'PASSWORD': '0000',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')

CKEDITOR_UPLOAD_PATH = 'uploads/'
# MEDIA_ROOT = os


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


ACCOUNT_AUTHENTICATION_METHOD = 'username'

# The URL to redirect to after a successful e-mail confirmation, in case no
# user is logged in. Default value is settings.LOGIN_URL.
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL= settings.LOGIN_URL

# The URL to redirect to after a successful e-mail confirmation, in case of
# an authenticated user. Default is settings.LOGIN_REDIRECT_URL
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = LOGIN_REDIRECT_URL

# Determines the expiration date of email confirmation mails (# of days).
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3

# The user is required to hand over an e-mail address when signing up.
ACCOUNT_EMAIL_REQUIRED = False

# Determines the e-mail verification method during signup. When set to
# "mandatory" the user is blocked from logging in until the email
# address is verified. Choose "optional" or "none" to allow logins
# with an unverified e-mail address. In case of "optional", the e-mail
# verification mail is still sent, whereas in case of "none" no e-mail
# verification mails are sent.
ACCOUNT_EMAIL_VERIFICATION = "optional"

# Subject-line prefix to use for email messages sent. By default, the name
# of the current Site (django.contrib.sites) is used.
ACCOUNT_EMAIL_SUBJECT_PREFIX = 'portfolio account activation '

# A string pointing to a custom form class
# (e.g. 'myapp.forms.SignupForm') that is used during signup to ask
# the user for additional input (e.g. newsletter signup, birth
# date). This class should implement a `def signup(self, request, user)`
# method, where user represents the newly signed up user.
ACCOUNT_SIGNUP_FORM_CLASS = base.forms.CustomUserCreationForm

# When signing up, let the user type in their password twice to avoid typ-o's.
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = True

# Enforce uniqueness of e-mail addresses.
ACCOUNT_UNIQUE_EMAIL = True

# A callable (or string of the form 'some.module.callable_name') that takes
# a user as its only argument and returns the display name of the user. The
# default implementation returns user.username.
ACCOUNT_USER_DISPLAY= User.username

# An integer specifying the minimum allowed length of a username.
ACCOUNT_USERNAME_MIN_LENGTH = 1

# The user is required to enter a username when signing up. Note that the
# user will be asked to do so even if ACCOUNT_AUTHENTICATION_METHOD is set
# to email. Set to False when you do not wish to prompt the user to enter a
# username.
ACCOUNT_USERNAME_REQUIRED = True

# render_value parameter as passed to PasswordInput fields.
ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = False

# Request e-mail address from 3rd party account provider? E.g. using OpenID
# AX, or the Facebook 'email' permission.
SOCIALACCOUNT_QUERY_EMAIL = ACCOUNT_EMAIL_REQUIRED

# Attempt to bypass the signup form by using fields (e.g. username, email)
# retrieved from the social account provider. If a conflict arises due to a
# duplicate e-mail address the signup form will still kick in.
SOCIALACCOUNT_AUTO_SIGNUP = True

# Enable support for django-avatar. When enabled, the profile image of the
# user is copied locally into django-avatar at signup. Default is
# 'avatar' in settings.INSTALLED_APPS.
# SOCIALACCOUNT_AVATAR_SUPPORT= 'avatar'

# Dictionary containing provider specific settings.
# SOCIALACCOUNT_PROVIDERS = 'google'