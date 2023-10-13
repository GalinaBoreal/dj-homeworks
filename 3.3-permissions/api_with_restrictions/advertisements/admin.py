from django.contrib import admin
from advertisements.models import *


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'creator', 'title', 'description', 'status']