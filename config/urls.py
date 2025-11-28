"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import redirect
from django.views.static import serve
from django.urls import re_path as url
from django.contrib.sitemaps.views import sitemap
from .sitemaps import MyModelSitemap
from django.views.generic import TemplateView


from . import views

from main.views import main_main
from gallery.views import gallery_main
from account.views import account_main
from about_crew.views import about_crews



urlpatterns = [
    path('admin/', admin.site.urls),  # 관리자 페이지
    path('', main_main, name='main'),  # 메인 페이지
    path('ads.txt', views.Ads), 
    path('blog/', include('blog.urls')),
    path("robots.txt", views.robots),
    # path('docs/<int:doc_id>', views.docs_detail_view, name='doc_detail'),
    # path('docs/', views.docs_list, name='docs_list'),
    # path('markdownx/', include('markdownx.urls')),
    # path(".well-known/discord", views.discord),
    path("sitemap.xml", views.sitemap),
    path('about_crewone/', include('about_crewones.urls')),
    path('about_crews/', about_crews, name='about_crews'),
    path('about_crewones_setting/', include('about_crewones_settings.urls')),
    path('projects/', include('projects.urls')),
    #path('ranking/', include("ranking.urls")),
    path('notices/', include('notice.urls')),
    path('api/', include('api.urls')),
    path('accounts/', include("account.urls")),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]


def redirect_to_main(request, exception):
    return redirect("main")

handler404 = redirect_to_main

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)