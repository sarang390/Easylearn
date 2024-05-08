from django.db import models

# Create your models here.

class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)


class User(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE,default=1)
    username=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    photo=models.CharField(max_length=300)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)


class Complaint(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    date=models.CharField(max_length=100)
    complaint=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    reply=models.CharField(max_length=100)


class Review(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    review=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    rating=models.CharField(max_length=100)