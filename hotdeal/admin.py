from django.contrib import admin
from hotdeal.models import Hotdeal


@admin.register(Hotdeal)
class HotdealAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['title']
    search_fields = ["title"]
