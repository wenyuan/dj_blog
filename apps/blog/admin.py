# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models

# Register your models here.


class EntryAdmin(admin.ModelAdmin):

    list_display = ['title', 'author', 'visiting', 'created_time', 'updated_time']


admin.site.register(models.Category)
admin.site.register(models.Tag)
admin.site.register(models.Entry, EntryAdmin)
