from django.db import models



class Project(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=100)
    start_date = models.DateField()


    class Meta():
        db_table = 'project'
# Create your models here.
