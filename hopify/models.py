from django.db import models
from django.contrib.auth.models import User
from .category import Category
import datetime
from PIL import Image

# Create your models here.

class  Signup(models.Model):
        id = models.AutoField(primary_key=True)
        username =  models.CharField(max_length = 255)
        password = models.CharField(max_length = 20)
        confirmpassword =models.CharField(max_length = 20,)
        email = models.EmailField(max_length= 50,null = True)
        firstname = models.CharField(max_length=200)  
        lastname = models.CharField(max_length=20) 
        #myimage = models.ImageField(blank=True, upload_to="profilepics")
        
  
        
        def __str__(self):
            return str(self.username)


class  Mylogin(models.Model):
    username =  models.CharField(max_length = 255)
    password = models.CharField(max_length = 20)




class Contact(models.Model):
    name= models.CharField(max_length=100)
    email=models.CharField(max_length=30)
    phone=models.CharField(max_length=12)
    message=models.TextField(max_length=500)
    date=models.DateField()


    def __str__(self):
        return str(self.name)



class Editprofile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,)
    image = models.ImageField(default='default.jpg',upload_to='profilepics')
    phone = models.IntegerField(default='0091')        
    def __str__(self):
        return f'{self.user.username} Editprofile'        


class Subscriberemail(models.Model):
    subscriber_mail_ids = models.CharField(max_length=30)


    def __str__(self):
        return str(self.subscriber_mail_ids)


class Product(models.Model): 
    name = models.CharField(max_length=200)  
    image = models.ImageField(blank=True, upload_to="products",default="")  
    category = models.ForeignKey(Category,on_delete=models.CASCADE,)
    description = models.CharField(max_length=200,null=True)
    price = models.FloatField()
    address = models.CharField(max_length=200)
    mobileno = models.IntegerField()   

    def __str__(self):
        return str(self.name)


    def save(self):
        super().save()   

        img = Image.open(self.image.path)

        if img.height > 600 or img.width > 600:
            output_size = (600, 600)
            img.thumbnail(output_size)
            img.save(self.image.path)

