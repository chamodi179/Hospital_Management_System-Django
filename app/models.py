from django.db import models

class HMS_User(models.Model):
    userId = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    contact = models.CharField(max_length=20)
    age = models.IntegerField()
    password = models.CharField(max_length=100)

def __str__(self):
    return self.first_name

#superuser credentionals--username (chamodi1999), password(chamodi1999)