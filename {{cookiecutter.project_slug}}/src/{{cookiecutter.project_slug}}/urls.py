from django.conf import settings
from django.contrib import admin
from django.urls import include, path
{% if cookiecutter.include_wagtail == "y" %}
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.contrib.sitemaps.views import sitemap
from wagtail.core import urls as wagtail_urls{% endif %}

urlpatterns = [
    path("admin/", admin.site.urls),
]

{% if cookiecutter.include_wagtail == "y" %}# Wagtail urls
urlpatterns += [
    path("sitemap.xml", sitemap, name="sitemap"),
    path("cms/", include(wagtailadmin_urls)),
    path("", include(wagtail_urls)),
]

{% endif %}if settings.DEBUG:
    import debug_toolbar  # noqa

    from django.conf.urls.static import static  # noqa
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns  # noqa

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
