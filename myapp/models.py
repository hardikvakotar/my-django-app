from __future__ import unicode_literals  
from django.db import models  
  
class Student(models.Model):  
    firstname = models.CharField(max_length=50)  
    lastname  = models.CharField(max_length = 10)  
    email     = models.EmailField()
    class Meta:  
        db_table = "student"  