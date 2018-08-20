from django.db import models

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    section = models.CharField(max_length=2)
    father_name = models.CharField(max_length=30)
    roll_no = models.IntegerField()

    def __str__(self):
        return(self.id,self.first_name)


