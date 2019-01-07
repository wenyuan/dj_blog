"""dj_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap

from project_apps.blog.models import Entry
from project_apps.blog.feed import LatestEntriesFeed
from project_apps.blog import views as blog_views

info_dict = {
    'queryset': Entry.objects.all(),
    'date_field': 'modified_time'
}

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', blog_views.index),
    url(r'^blog/', include('project_apps.blog.urls')),
    url(r'^latest/feed/$', LatestEntriesFeed()),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}},
        name='django.contrib.sitemaps.views.sitemap'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler403 = blog_views.permission_denied
handler404 = blog_views.page_not_found
handler500 = blog_views.page_error
