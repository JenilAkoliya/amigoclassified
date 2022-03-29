from django import forms
from .models import  Signup
from .models import  Mylogin
from .models import Editprofile
from .models import Product


from django.contrib.auth.models import User


class SignupForm(forms.ModelForm):
    class Meta:
        model  = Signup
        fields = "__all__" 
        #exclude = ['user']

        widgets = {

            'username': forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter username','id':'username'}),
            'password' : forms.TextInput(attrs = {'type':'password','class':'form-control','id':'password','placeholder':'Enter password'}),
            'confirmpassword' : forms.TextInput(attrs = {'type':'password','class':'form-control','id':'confirmpassword','placeholder':'Retype password'}),
            'email': forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter email','type':'email'}),
            'firstname' : forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter first name'}),
            'lastname' : forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter last name'}),

            }


class MyloginForm(forms.ModelForm):
    class Meta:
        model  = Mylogin
        fields = "__all__" 

        widgets = {

            'username': forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter username',}),
            'password' : forms.TextInput(attrs = {'type':'password','class':'form-control','placeholder':'Enter password'}),     

            }



class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name']

        widgets = {

            'username': forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter username',}),
            'email' : forms.TextInput(attrs = {'type':'email','class':'form-control','placeholder':'Enter email'}),     
            'first_name' : forms.TextInput(attrs = {'type':'text','class':'form-control','placeholder':'First name'}),
            'last_name' : forms.TextInput(attrs = {'type':'text','class':'form-control','placeholder':'Last name'}),     

            }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Editprofile
        fields = ['image','phone']

        widgets = {

            'phone' : forms.TextInput(attrs = {'type':'tel','class':'form-control','placeholder':'phone'}),     

            }

class ProductForm(forms.ModelForm):
    class Meta:
        model  = Product
        fields = "__all__" 


        widgets = {

            'name': forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter product name',}),
            'description': forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter description',}),
            'price': forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter sell price',}),
            'address': forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter address',}),
            'mobileno': forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter your mobile',}),


            }
