from django.db import models

# Create your models here.

class Enquiry(models.Model):
    name = models.CharField(max_length=60)
    contact = models.CharField(max_length=10)
    emailid = models.CharField(max_length=60)
    age = models.CharField(max_length=40)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    unit = models.CharField(max_length=10)
    date = models.CharField(max_length=40)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Plan(models.Model):
    name = models.CharField(max_length=60)
    amount = models.CharField(max_length=10)
    duration = models.CharField(max_length=60)
    
    
    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=60)
    contact = models.CharField(max_length=10)
    emailid = models.CharField(max_length=60)
    age = models.CharField(max_length=40)
    gender = models.CharField(max_length=10)
    plan = models.CharField(max_length=50)
    joindate = models.CharField(max_length=40)
    expiredate = models.CharField(max_length=40)
    initialamount = models.CharField(max_length=10)


    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100, null=True,blank=True)
    emailid = models.CharField(max_length=50, null=True)
    contact = models.CharField(max_length=15, null=True)
    subject = models.CharField(max_length=100, null=True)
    message = models.CharField(max_length=300, null=True)
    msgdate = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    isread = models.BooleanField(default=False,blank=True,null=True)
    def __str__(self):
        return self.name
