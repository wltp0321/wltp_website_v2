# views.py
from django.shortcuts import render
from .models import aboutCrew

def about_crews(request):
    about_crew = aboutCrew.objects.all()
    return render(request, 'about_crew/about_crew.html', {'about_crew': about_crew})
