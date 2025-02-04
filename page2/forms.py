from django import forms
from . models import Project
class PageForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        widgets = {
            'p_name': forms.TextInput(attrs={'class': 'form-control p-3 mt-4','placeholder':"Enter project name"}),
            'start_date': forms.DateInput(attrs={'class': 'form-control p-3 mt-4', 'type': 'date',"placeholder":"Enter start_date"}),
        }
        labels = {
            field: ""
            for field in ['p_name','start_date']
        }
