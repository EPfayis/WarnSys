from django.urls import path,include
from locations import views

urlpatterns = [

    path("mainlocations/",views.ClsMainLocation.as_view(),name= "mainlocations"),
    path("sublocations/",views.ClsSubLocations.as_view(),name= "sublocations"),

]

