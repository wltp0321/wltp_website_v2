# models.py
from django.db import models

class aboutCrewonessSettings(models.Model):
    name = models.TextField("name", null=True, blank=True)
    pc_stat = models.TextField("pc_stat", null=True, blank=True)
    game_setting = models.TextField("game_setting", null=True, blank=True)

    class Meta:
        ordering = ['id']  
        
    def __str__(self):
        return f"{self.name} | {self.pc_stat[:20]} | {self.game_setting[:20]}"

