from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required

from datetime import datetime



from hopify.models import Signup,Mylogin,Contact,Editprofile,Subscriberemail
from hopify.models import Product,Category

from .forms import SignupForm,MyloginForm,UserUpdateForm,ProfileUpdateForm,ProductForm



from django.contrib import messages
from django.db.models import Q


# Create your views here.



class index(View):
    def get(self,request):
        show = Category.objects.all()
        d= {'category':show}
        return render(request,'index.html',d)


def contact(request):
    if request.method =='GET':
        return render(request,'contact.html')

def about(request):
    if request.method =='GET':
        return render(request,'about.html')

def clients(request):
    if request.method =='GET':
        return render(request,'clients.html')


def browseads(request):
    if request.method =='GET':
        show = Category.objects.all()
        d= {'category':show}
        return render(request,'browseads.html',d)

        


def signup(request):
    if request.method =='GET':
        sfm = SignupForm()
        d = {'form':sfm}
        return render(request,"signup.html",d)



    if request.method == 'POST':
        res = SignupForm(request.POST,request.FILES)
        
        if res.is_valid():
            username = res.cleaned_data['username']
            password = res.cleaned_data['password']
            confirmpassword = res.cleaned_data['confirmpassword']
            email = res.cleaned_data['email']
            firstname = res.cleaned_data['firstname']
            lastname = res.cleaned_data['lastname']

           
            if password != confirmpassword:
                messages.error(request, 'password doesnt match')
                return redirect('signup')
        user = User.objects.create_user(email=email,username=username,password=password,first_name=firstname,last_name=lastname,)
        user.save()
        messages.success(request,'you have sign up succesfully')
        new_user = authenticate(username=res.cleaned_data['username'],
                                    password=res.cleaned_data['password'],
                                    )
        login(request,new_user)
        return redirect('index')               


def mylogin(request):
    if request.method =='GET':
        sfm = MyloginForm()
        d = {'form':sfm}
        return render(request,"mylogin.html",d)


    if request.method =="POST":
        rem = MyloginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user) 
            return render(request, 'index.html')

        else:
            messages.warning(request, 'Invalid credentials,try valid input data')
            return redirect('mylogin')

def logoutuser(request):
    logout(request)
    return redirect("/")


def myprofile(request):
    userprofiledata = User.objects.filter(username = request.user.username).values()
    d = {'userdata':userprofiledata}
    messages.success(request, 'Logged in successfully.')
    return render(request, 'myprofile.html',d)



def contact(request):
    if request.method == "POST": 
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name = name,email = email, phone = phone, message = message , date = datetime.today())
        contact.save()
        messages.success(request, 'Contact submitted successfully.')
        return redirect('contact')


    else:
        return render(request,'contact.html')


def editprofile(request):
    if request.method=="POST":
        u_form = UserUpdateForm(request.POST,instance= request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance = request.user.editprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('myprofile')


    else:
        u_form = UserUpdateForm(instance= request.user)
        p_form = ProfileUpdateForm(instance = request.user.editprofile)
        context = {
            'u_form': u_form,
            'p_form': p_form
        }
        return render(request,'editprofile.html',context)        


def subscriberemail(request):
    if request.method == "POST":
        subscriberemail = request.POST.get("subemail")
        emaildata = Subscriberemail(subscriber_mail_ids=subscriberemail)
        emaildata.save()
        message="We have received a mail-id.Thanks to our new subscriber"
        messages.success(request, 'Thanks for subscribing our service.')
        return render(request, "about.html")


    else:
        return render(request, "index.html")



def showproduct(request):
    if request.method=='GET':
        # show = Product.objects.all().order_by('name')
        show = Product.objects.all().order_by('-id')
        d = {"products":show}
        return render(request,'showproduct.html',d)





def category(request,id):
    if request.method=='GET':
        show = Product.objects.filter(category=id).order_by('-id')
        d = {"products":show}
        return render(request,'category.html',d)


def searchproduct(request):
    if request.method == 'POST':
        name  = request.POST['ename']
        # sproducts = Product.objects.filter(name__icontains=name)        
        sproducts = Product.objects.filter(
            Q(name__icontains=name) | Q(address__icontains=name) | Q(description__icontains=name)  | Q(name__istartswith=name[:2]) | Q(address__istartswith=name[:3]) | Q(description__istartswith=name[:3])
            )    
        d = {'products':sproducts}     
        return render(request,"showproduct.html",d)

    else:
        pass


@login_required(login_url ='/mylogin/')
def uploadproduct(request):
    if request.method == 'GET':
        upload_form = ProductForm()
        d = {'form':upload_form}
        return render(request,'uploadproduct.html',d)


    if request.method == 'POST':
        upload_form = ProductForm(request.POST,request.FILES)
        if upload_form.is_valid:
            upload_form.save()
            return redirect('showproduct')



def productdetail(request,id):
    if request.method=="GET":
        data = Product.objects.filter(id = id)
        d={'productdetail':data}
        return render(request,'productdetail.html',d)