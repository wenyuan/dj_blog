# -*- coding: utf-8 -*-

from django.contrib.syndication.views import Feed
# from django.urls import reverse
from .models import Entry


class LatestEntriesFeed(Feed):
    title = "我的博客网站"
    link = "/siteblogs/"
    description = "最新更新的博客文章！"

    def items(self):
        return Entry.objects.order_by('-created_time')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.abstract

    # item_link is only needed if entries has no get_absolute_url method.
    # def item_link(self, item):
    #     return reverse('news-item', args=[item.pk])
