# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name=_('category'))

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        verbose_name = 'category'
        verbose_name_plural = verbose_name


class Tag(models.Model):
    name = models.CharField(max_length=128, verbose_name=_('tag'))

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tag'
        verbose_name = 'tag'
        verbose_name_plural = verbose_name


class Entry(models.Model):
    title = models.CharField(max_length=128, verbose_name=_('blog title'))
    author = models.ForeignKey(User, verbose_name=_('blogger'))  # 一对多
    img = models.ImageField(upload_to='blog_imgs', null=True, blank=True, verbose_name=_('blog img'))
    body = models.TextField(verbose_name=_('blog body'))
    abstract = models.TextField(max_length=256, blank=True, null=True, verbose_name=_('blog abstract'))
    visiting = models.PositiveIntegerField(default=0, verbose_name=_('blog visiting'))
    categories = models.ManyToManyField('Category', verbose_name=_('blog categories'))
    tags = models.ManyToManyField('Tag', verbose_name=_('blog tags'))
    created_time = models.DateTimeField(auto_now_add=True, verbose_name=_('created time'))
    updated_time = models.DateTimeField(auto_now=True, verbose_name=_('updated time'))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog_detail', kwargs={'blog_id': self.id})  # http://127.0.0.1/blog/3

    def increase_visiting(self):
        self.visiting += 1
        self.save(update_fields=['visiting'])

    class Meta:
        db_table = 'entry'
        verbose_name = _('blog')
        verbose_name_plural = verbose_name
        ordering = ['-created_time']
