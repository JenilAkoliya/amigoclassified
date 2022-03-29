from django.contrib import admin
from hopify.models import Signup
from hopify.models import Mylogin
from hopify.models import Contact
from hopify.models import Editprofile
from hopify.models import Subscriberemail
from hopify.models import Product
from hopify.models import Category

class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','category']

# Register your models here.

admin.site.register(Signup)
admin.site.register(Mylogin)
admin.site.register(Contact)
admin.site.register(Editprofile)
admin.site.register(Subscriberemail)
admin.site.register(Product,AdminProduct)
admin.site.register(Category)



