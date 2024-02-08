from django.db import models

# Create your models here.
class Contact(models.Model):
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=12)
    
    def __str__(self):
        return self.email