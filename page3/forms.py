from django import forms 
from . models import Department

class DepForm(forms.ModelForm):
    class Meta():
        model = Department
        fields = '__all__'
        widgets = {
            'dep_id': forms.TextInput(attrs={'class': 'form-control'}),
            'dept_name': forms.TextInput(attrs={'class': 'form-control'}),
            'manager_id': forms.TextInput(attrs={'class': 'form-control'}),
        }