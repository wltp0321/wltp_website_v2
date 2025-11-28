from django import forms
from .models import ImportantNotice, NormalNotice, ArchivedNotice

# 공지 작성 및 수정용 폼
class NoticeForm(forms.ModelForm):
    class Meta:
        fields = ['title', 'content0', 'content1']


# 이동용 폼 (카테고리 전환)
class NoticeMoveForm(forms.Form):
    CATEGORY_CHOICES = [
        ('important', '중요 공지'),
        ('normal', '일반 공지'),
        ('archived', '아카이브'),
    ]
    target = forms.ChoiceField(choices=CATEGORY_CHOICES, label='이동할 분류')
