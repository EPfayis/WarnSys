from django.contrib.auth.hashers import make_password

from .models import User
from .models import TblUserDetails
from WarnSys.Imports import *



def getUserDetails(obj_user):
    obj_user_details = TblUserDetails.objects.filter(user=obj_user)
    if obj_user_details.count() == 0:
        return None
    return obj_user_details.first()



class UserValidator():

    is_superuser = False
    is_anonymouse = False
    user = None
    user_det = None

    def __init__(self,obj_user):

        self.user = obj_user

        if str(obj_user) == "AnonymousUser":
            self.is_anonymouse = True
            return

        if obj_user.is_superuser == True:
            self.is_superuser = True


        self.user_det = getUserDetails(obj_user)


def createSuperUser():

    obj_user = User()
    obj_user.is_superuser = True
    obj_user.first_name = "admin"
    obj_user.username = "admin"
    obj_user.email = ""
    obj_user.password = make_password("123123")
    obj_user.save()
    print("admin account created")