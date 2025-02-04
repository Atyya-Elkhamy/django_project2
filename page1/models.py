from django.db import models
# from page2.models import Project
# from page3.models import Department

class Emp(models.Model):
    emp_id = models.AutoField(primary_key=True)
    f_name = models.CharField(max_length=50 ,null=False)
    l_name = models.CharField(max_length=50 , null=False)
    age = models.IntegerField(null=False)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField(unique=True ,null=False)
    dept_id = models.ForeignKey('page3.Department',on_delete=models.SET_NULL, null=True ,to_field='dept_id')
    project_id = models.ForeignKey('page2.Project', on_delete=models.SET_NULL, null=True,to_field='p_id')
    def __str__(self):
        return self.f_name
    class Meta():
        db_table = 'employee'
        

# Create your models here.