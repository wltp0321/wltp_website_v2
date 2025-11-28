from django import forms
from .models import aboutCrewonessSettings

class CrewSettingForm(forms.ModelForm):
    class Meta:
        model = aboutCrewonessSettings
        fields = ['name', 'pc_stat', 'game_setting']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full p-3 border rounded-md'}),
            'pc_stat': forms.Textarea(attrs={'class': 'w-full p-3 border rounded-md', 'rows': 3}),
            'game_setting': forms.Textarea(attrs={'class': 'w-full p-3 border rounded-md', 'rows': 5}),
        }
