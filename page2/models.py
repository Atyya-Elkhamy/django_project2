from django.db import models



class Project(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=100 ,null=False)
    start_date = models.DateField(null=False)
    def __str__(self):
        return self.p_name

    class Meta():
        db_table = 'project'
# Create your models here.
