from django.urls import path, include

from camera import views

urlpatterns = [

    path('', views.ClsCamera.as_view(), name="camera"),

]


