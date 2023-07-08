from django import forms
from todolist.models import Items

class ItemsForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
