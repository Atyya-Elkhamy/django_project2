from django import forms 
from . models import Department

class DepForm(forms.ModelForm):
    class Meta():
        model = Department
        fields = '__all__'
        widgets = {
            field: forms.TextInput(attrs={'class': 'form-control p-3 mt-4',"placeholder":f"Enter {field}"})
            for field in ['dep_id','dept_name','manager_id']
        }
        labels ={
            field : "" 
            for field in ['dep_id','dept_name','manager_id']
        }
        # widgets = {
        #     'dep_id': forms.TextInput(attrs={'class': 'form-control'}),
        #     'dept_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'manager_id': forms.TextInput(attrs={'class': 'form-control'}),
        # }