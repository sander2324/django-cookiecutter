import os
from pathlib import Path

import environ

env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

AUTH_USER_MODEL = "user.User"


# Application definition

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",{% if cookiecutter.include_wagtail == "y" %}
    "wagtail.contrib.modeladmin",
    "wagtail.contrib.settings",
    "wagtail.contrib.redirects",
    "wagtail.contrib.routable_page",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail.core",
    "modelcluster",
    "taggit",{% endif %}
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",{% if cookiecutter.include_drf == "y" %}
    "rest_framework",{% endif %}
    "{{cookiecutter.project_slug}}",
    "{{cookiecutter.project_slug}}.apps.user",{% if cookiecutter.include_wagtail == "y" %}
    "{{cookiecutter.project_slug}}.apps.cms",{% endif %}
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",{% if cookiecutter.include_wagtail == "y" %}
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",{% endif %}
]

ROOT_URLCONF = "{{cookiecutter.project_slug}}.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

MEDIA_URL = env.str("MEDIA_URL", default="/media/")
MEDIA_ROOT = os.path.join(BASE_DIR, "public/media")

WSGI_APPLICATION = "{{cookiecutter.project_slug}}.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {"default": env.db_url()}


# Cache
# https://docs.djangoproject.com/en/3.1/ref/settings/#std:setting-CACHES

CACHES = {"default": env.cache(default="dummycache://")}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

LANGUAGE_COOKIE_SECURE = True

EMAIL_USE_TLS = True


# Cors

CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = env.list("CORS_ORIGIN_WHITELIST", default=[])

{% if cookiecutter.include_wagtail == "y" %}# Wagtail

BASE_URL = env.str("BASE_URL", default="http://localhost:8000")

WAGTAIL_SITE_NAME = "{{cookiecutter.project_title}}"
WAGTAILADMIN_NOTIFICATION_USE_HTML = True

WAGTAILIMAGES_JPEG_QUALITY = 60  # Default is 85
WAGTAILIMAGES_MAX_UPLOAD_SIZE = 15 * 1024 * 1024  # 10 Mb

WAGTAIL_USAGE_COUNT_ENABLED = False


{% endif %}# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [os.path.join(BASE_DIR, "locales")]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = env.str("STATIC_URL", default="/static/")
STATIC_ROOT = os.path.join(BASE_DIR, "public/static")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
