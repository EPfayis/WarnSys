from django.urls import path, include

from user import views

urlpatterns = [

    path('profile/', views.ClsUser.as_view(), name="users"),
    path('login/', views.ClsLogin.as_view(), name="login"),
]


