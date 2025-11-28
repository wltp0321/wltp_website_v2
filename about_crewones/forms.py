from django import forms
from .models import CrewMember

class CrewMemberForm(forms.ModelForm):
    class Meta:
        model = CrewMember
        fields = ['name', 'position', 'description', 'image', 'order']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'border rounded-lg p-2 w-full'}),
            'position': forms.TextInput(attrs={'class': 'border rounded-lg p-2 w-full'}),
            'description': forms.Textarea(attrs={'class': 'border rounded-lg p-2 w-full', 'rows':4}),
            'order': forms.NumberInput(attrs={'class': 'border rounded-lg p-2 w-full'}),
        }
