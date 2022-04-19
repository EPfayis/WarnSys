from django.shortcuts import render
from WarnSys.Imports import *
from .serializers import *
from .models import *
# Create your views here.


class ClsUser(ListAPIView):

    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def post(self,request):

        lst_model_objects = []

        try:
            obj_requested_user = self.request.user
            user_validator = UserValidator(obj_requested_user)


            name = request.data["name"]
            email = request.data["email"]
            mobile = request.data["mobile"]
            username = request.data["username"]
            password = request.data["password"]
            print("request accepted")


            if name == "":
                return JsonResponse(getValErrorDict("invalid name"))
            if email == "":
                return JsonResponse(getValErrorDict("invalid email"))
            if mobile == "":
                return JsonResponse(getValErrorDict("invalid mobile"))
            if username == "":
                return JsonResponse(getValErrorDict("invalid username"))
            if password == "":
                return JsonResponse(getValErrorDict("invalid password"))
            print("request validated")


            obj_user = User()
            obj_user.first_name = name
            obj_user.email = email
            obj_user.username = username
            obj_user.password = make_password(password)
            obj_user.save()
            lst_model_objects.append(obj_user)
            print("user created")


            obj_userdetails = TblUserDetails()
            obj_userdetails.user = obj_user
            obj_userdetails.mobile = mobile
            obj_userdetails.save()
            lst_model_objects.append(obj_userdetails)
            print("user details saved")



            token, created = Token.objects.get_or_create(user= obj_user)

            return JsonResponse(getSuccessDict("user creation completed",{"token" : "Token " + str(token.key),"id" : obj_user.id}))


        except Exception as e:
            for i in reversed(lst_model_objects):
                i.delete()
            return JsonResponse(getErrorDict("an error occured",str(e)))

    def get_queryset(self):

        try:
            objUser = self.request.user
            userValidator = UserValidator(objUser)
            print("User Identification Completed")

            if userValidator.is_superuser == False:
                "Normal user can only see their own profile"
                return User.objects.filter(id= objUser.id)

            "if execution reached here, then requested user is admin"

            searchText = self.request.GET.get("searchText","")
            print("Request Accepted")

            qsUser = User.objects.all()

            if searchText != "":
                lst_user_id = TblUserDetails.objects.filter(mobile__contains=searchText).values_list("user_id",flat=True)
                qsUser = qsUser.filter(Q(first_name__icontains= searchText) | Q(id__in=lst_user_id))

            return qsUser


        except Exception as e:
            print("Exception occured : ", str(e))
            return User.objects.none()

class ClsLogin(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})

        if serializer.is_valid(raise_exception=False) == True:
            user = serializer.validated_data['user']
            user_validator = UserValidator(user)
            token, created = Token.objects.get_or_create(user=user)

            mobile = ""

            if user_validator.user_det != None:
                mobile = user_validator.user_det.mobile

            return Response({
                STATUS : True,
                'token': "Token " + token.key,
                'user_id': user.pk,
                'name': user.first_name,
                'email': user.email,
                'mobile': mobile,
                "is_superuser" : user_validator.is_superuser,
            })
        else:
            print(serializer.data)
            return JsonResponse(getValErrorDict("invalid username or password"))
