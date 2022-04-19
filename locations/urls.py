from django.urls import path,include
from locations import views

urlpatterns = [

    path("",views.ClsMainLocation.as_view(),name= "mainlocations"),


]

