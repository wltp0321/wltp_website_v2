from django.urls import path
from . import views

app_name = 'about_crew'

urlpatterns = [
    path('', views.crew_settings_list, name='list'),
    path('create/', views.crew_setting_create, name='create'),
    path('<int:pk>/', views.crew_setting_detail, name='detail'),
    path('<int:pk>/edit/', views.crew_setting_edit, name='edit'),
    path('<int:pk>/delete/', views.crew_setting_delete, name='delete'),
]
