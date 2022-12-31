from django.contrib import admin
from . import models as appmodels


@admin.register(appmodels.Menu)
class MenuAdmin(admin.ModelAdmin):
    ordering = ['name']


@admin.register(appmodels.Relationship)
class MenuAdmin(admin.ModelAdmin):
    ordering = ['parent']
