from django.db import models

class Member(models.Model):
    membership_id =models.CharField(max_length=5, unique=True) 
    part = models.CharField(max_length=15)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    programme = models.CharField(max_length=25)
    level = models.IntegerField()
    address = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="profile", null=True, blank=True)
    registration_date = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.membership_id


class Contact(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title