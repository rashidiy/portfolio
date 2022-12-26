from django.contrib import admin
from django.contrib.admin import ModelAdmin

from portfolio.models import Portfolio, Post, Contact


# Register your models here.
@admin.register(Portfolio)
class PortfolioAdmin(ModelAdmin):
    list_display = ('title',)


@admin.register(Post)
class PortfolioAdmin(ModelAdmin):
    list_display = ('title',)


@admin.register(Contact)
class PortfolioAdmin(ModelAdmin):
    list_display = ('name', 'email')
