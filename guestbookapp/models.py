from django.db import models

class Book(models.Model):
    message = models.CharField(max_length=200)
    pub_person = models.CharField(max_length=5)
    pub_date = models.DateField('date published')
    
     