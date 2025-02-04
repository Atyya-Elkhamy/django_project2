from django import forms
from . models import Emp

class EmpForm(forms.ModelForm):
    class Meta:
        model = Emp
        fields = '__all__'
        widgets = {
            field: forms.TextInput(attrs={'class': 'form-control mt-4 p-3', 'placeholder': f"Enter your {field}"})
            for field in ['f_name', 'l_name', 'salary', 'age', 'email', 'dept_id', 'project_id']
        }
        labels = {
            field: ''
            for field in ['f_name', 'l_name', 'salary', 'age', 'email', 'dept_id', 'project_id']
        }
        # widgets = {
        #     'f_name': forms.TextInput(attrs={'class': 'form-control mt-4 p-3','placeholder':"Enter First Name"}),
        #     'l_name': forms.TextInput(attrs={'class': 'form-control mt-4 p-3','placeholder':"Enter last Name"}),
        #     'salary': forms.TextInput(attrs={'class': 'form-control mt-4 p-3','placeholder':"Enter salary"}),
        #     'age': forms.TextInput(attrs={'class': 'form-control mt-4 p-3','placeholder':"Enter your age"}),
        #     'email': forms.TextInput(attrs={'class': 'form-control mt-4 p-3','placeholder':"Enter your Email"}),
        #     'dept_id': forms.TextInput(attrs={'class': 'form-control mt-4 p-3','placeholder':"Enter dept_id"}),
        #     'project_id': forms.TextInput(attrs={'class': 'form-control mt-4 p-3','placeholder':"Enter project_id"}),
        # }
        
        # labels = {
        #     'f_name': '',
        #     'l_name': '',
        #     'salary': '',
        #     'age': '',
        #     'email': '',
        #     'dept_id': '',
        #     'project_id': '',
        # }
        # exclude = None
        # labels = None
        # help_texts = None
        # error_messages = None
        # widgets = None
        # localized_fields = None
        # field_classes = None
        # formfield_callback = None