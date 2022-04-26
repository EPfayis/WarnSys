from django.urls import path, include

from alert import views

urlpatterns = [

    path('', views.ClsAlert.as_view(), name="alert"),

]


