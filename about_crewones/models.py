from django.db import models

class CrewMember(models.Model):
    name = models.CharField("이름", max_length=50)
    position = models.CharField("역할", max_length=50, blank=True)
    description = models.TextField("소개", blank=True)
    image = models.ImageField("프로필 이미지", upload_to="crew_images/", blank=True, null=True)
    order = models.PositiveIntegerField("정렬 순서", default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name
