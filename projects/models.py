from django.db import models

STATUS_CHOICES = [
    ('진행중', '진행중'),
    ('완료', '완료'),
    ('중지', '중지'),
]

class Project(models.Model):
    name = models.CharField("프로젝트명", max_length=200)
    description = models.TextField("설명", blank=True, null=True)
    status = models.CharField("상태", max_length=10, choices=STATUS_CHOICES, default='진행중')
    github_repo = models.CharField("GitHub Repo (owner/repo)", max_length=200, blank=True, null=True)
    detail_url = models.URLField("외부 링크", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return self.name
