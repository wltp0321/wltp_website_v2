# admin.py
from django.contrib import admin
from .models import aboutCrewonessSettings

@admin.register(aboutCrewonessSettings)
class aboutCrewonessSettingsAdmin(admin.ModelAdmin):
    list_display = ('name', 'pc_stat', 'game_setting')
