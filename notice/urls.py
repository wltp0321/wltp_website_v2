# notice/urls.py
from django.urls import path
from . import views

app_name = 'notice'

urlpatterns = [
    path('', views.notice_list, name='list'),  # 공지 목록
    path('archived/<int:notice_id>/', views.archived_notice, name='archived'),  # 아카이브 공지 상세
    path('create/', views.notice_create, name='create'),  # 공지 작성
    # urls.py
    path('<str:notice_type>/<int:notice_id>/edit/', views.notice_edit, name='edit'),

    path('<str:notice_type>/<int:notice_id>/delete/', views.notice_delete, name='delete'),

]
