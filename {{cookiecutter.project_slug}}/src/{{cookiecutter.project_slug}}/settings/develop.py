from .base import *  # noqa

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*"])  # noqa

DEBUG = True

SESSION_COOKIE_SECURE = False

CSRF_COOKIE_SECURE = False

LANGUAGE_COOKIE_SECURE = False

EMAIL_USE_TLS = False

CORS_ALLOW_ALL_ORIGINS = True

INSTALLED_APPS = INSTALLED_APPS + ["debug_toolbar"]  # noqa

MIDDLEWARE = MIDDLEWARE + ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa

INTERNAL_IPS = ["127.0.0.1"]

try:
    from .local import *  # noqa
except ImportError:
    pass
