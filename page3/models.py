from django.db import models
# from page1.models import Emp

class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=100)
    manager_id = models.ForeignKey('page1.Emp', on_delete=models.SET_NULL, null=True,to_field='emp_id')

    class Meta():
        db_table = 'department'
# Create your models here.
