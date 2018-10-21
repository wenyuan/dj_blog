# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Q
import markdown
import pygments

from . import models
from utils.pagination import make_paginator, pagination_data


def index(request):
    entries = models.Entry.objects.all()
    page = request.GET.get('page', 1)
    entry_list, paginator = make_paginator(entries, page)
    page_data = pagination_data(paginator, page)

    return render(request, 'blog/index.html', locals())


def detail(request, blog_id):

    # entry = models.Entry.objects.get(id=blog_id)
    entry = get_object_or_404(models.Entry, id=blog_id)
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    entry.body = md.convert(entry.body)
    entry.toc = md.toc
    entry.increase_visiting()

    return render(request, 'blog/detail.html', locals())


def category(request, category_id):
    # c = models.Category.objects.get(id=category_id)
    c = get_object_or_404(models.Category, id=category_id)
    entries = models.Entry.objects.filter(category=c)
    page = request.GET.get('page', 1)
    entry_list, paginator = make_paginator(entries, page)
    page_data = pagination_data(paginator, page)
    return render(request, 'blog/index.html', locals())


def tag(request, tag_id):
    # t = models.Tag.objects.get(id=tag_id)
    t = get_object_or_404(models.Tag, id=tag_id)
    if t.name == "全部":
        entries = models.Entry.objects.all()
    else:
        entries = models.Entry.objects.filter(tags=t)

    page = request.GET.get('page', 1)
    entry_list, paginator = make_paginator(entries, page)
    page_data = pagination_data(paginator, page)
    return render(request, 'blog/index.html', locals())


def search(request):

    keyword = request.GET.get('keyword', None)
    if not keyword:
        error_msg = "请输入关键字"
        return render(request, 'blog/index.html', locals())

    entries = models.Entry.objects.filter(Q(title__icontains=keyword)
                                          | Q(body__icontains=keyword)
                                          | Q(abstract__icontains=keyword))
    page = request.GET.get('page', 1)
    entry_list, paginator = make_paginator(entries, page)
    page_data = pagination_data(paginator, page)
    return render(request, 'blog/index.html', locals())


def archives(request, year, month):
    entries = models.Entry.objects.filter(created_time__year=year, created_time__month=month)
    page = request.GET.get('page', 1)
    entry_list, paginator = make_paginator(entries, page)
    page_data = pagination_data(paginator, page)
    return render(request, 'blog/index.html', locals())


def permission_denied(request):

    return render(request, 'blog/403.html', locals())


def page_not_found(request):

    return render(request, 'blog/404.html', locals())


def page_error(request):

    return render(request, 'blog/500.html', locals())
