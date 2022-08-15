from django.db import models

# Create your models here.
class Contact(models.Model):
    Fname=models.CharField(max_length=100)
    Lname=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Ramarks=models.TextField()

    def __str__(self):
        return self.Fname,self.Ramarks


class Signup(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.EmailField()
    mobile=models.PositiveIntegerField()
    gender=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    profile_pic=models.ImageField(upload_to='profile/')   
    def __str__(self):
            return self.email
