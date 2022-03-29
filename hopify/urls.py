from django.contrib import admin
from django.urls import path,include
from hopify import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index.as_view(),name='index'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('clients/',views.clients,name='clients'),
    path('browseads/',views.browseads,name='browseads'),
    path('signup/',views.signup,name='signup'),
    path('mylogin/',views.mylogin,name='mylogin'),
    path('logoutuser/',views.logoutuser,name='logoutuser'),
    path('myprofile/',views.myprofile,name='myprofile'),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('subscriberemail/',views.subscriberemail,name='subscriberemail'),
    path('showproduct/',views.showproduct,name='showproduct'),

###############################categories###############################################3
    path('category/<int:id>',views.category,name='category'),
    path('searchproduct/',views.searchproduct,name='searchproduct'),
    path('uploadproduct/',views.uploadproduct,name='uploadproduct'),
    path('productdetail/<int:id>',views.productdetail,name='productdetail'),





]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)