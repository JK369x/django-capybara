from django.db import models
from django.contrib.auth.models import User

# Create your models here.
'''
Product
    - title (Char)
    - description (Text)
    - price (decimal)
    - quantity (Int)
'''

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) #null อณุญาติให้ data base เป็น null blank ค่าว่างได้
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    
    def __str__(self): #function พิเศษ
        return self.title
'''
    Contact
        - title (Char)
        - email (Char)
        - description (Text)
'''

class ContactUs(models.Model):
    title = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    check_box = models.BooleanField(default=False)
    
    def __str__(self): #function พิเศษ
        return self.title
    
'''
    - user 
    - usertype (char)
    - point (int)
'''

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  #เมื่อกำหนดสิทใหม่จะลบสิทเก่า
    usertype = models.CharField(max_length=100,default='member')
    point = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user.username + self.usertype
    
    

    