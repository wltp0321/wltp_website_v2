from django.urls import path
from . import views

app_name = 'about_crewones'

urlpatterns = [
    path('', views.crew_list, name='crew_list'),
    path('add/', views.add_crew, name='add_crew'),
    path('<int:pk>/edit/', views.edit_crew, name='edit_crew'),
    path('<int:pk>/delete/', views.delete_crew, name='delete_crew'),
]
