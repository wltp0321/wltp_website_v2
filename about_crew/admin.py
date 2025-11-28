# admin.py
from django.contrib import admin
from .models import aboutCrew

@admin.register(aboutCrew)
class aboutCrewAdmin(admin.ModelAdmin):
    list_display = ('order', 'emoji', 'title', 'content')
