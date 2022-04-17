from django.shortcuts import render
from WarnSys.Imports import *
from .models import *
from .serializer import *

# Create your views here.

class ClsMainLocation(ListAPIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    serializer_class = MainLocationSerializer

    def post(self, request):

        try:

            obj_user = self.request.user
            user_validator = UserValidator(obj_user)

            name = request.data["name"]
            is_active = True
            print("request accepted")


            if user_validator.is_superuser == False:
                return JsonResponse(getValErrorDict("you are not identified as admin"))
            if name == "":
                return JsonResponse(getValErrorDict("invalid name"))
            if TblMainLocations.objects.filter(name__iexact= name).count() > 0:
                return JsonResponse(getValErrorDict("location already found in this name"))
            print("request validated")


            obj_mainlocation = TblMainLocations()
            obj_mainlocation.name = name
            obj_mainlocation.is_active = is_active
            obj_mainlocation.save()
            print("main location saved")


            return JsonResponse(getSuccessDict("main location saved",{"id" : obj_mainlocation.id}))



        except Exception as e:
            return JsonResponse(getErrorDict("an error occured",str(e)))

    def get_queryset(self):

        try:

            obj_user = self.request.user
            user_validator = UserValidator(obj_user)
            print("user identified")


            is_active = self.request.GET.get("is_active","")
            search_text = self.request.GET.get("search_text","")
            page_wise = self.request.GET.get("page_wise","true")
            print("request accepted")


            if is_active not in lst_string_bool_values_with_blank:
                return TblMainLocations.objects.none()
            if page_wise not in lst_string_bool_values_without_blank:
                return TblMainLocations.objects.none()
            print("request validated")


            qs = TblMainLocations.objects.all()

            if get_bool_of_string(page_wise) == False:
                self.pagination_class = None
            if user_validator.is_superuser == False:
                qs = qs.filter(is_active= True)
            if is_active != "":
                qs = qs.filter(is_active= get_bool_of_string(is_active))


            qs = qs.filter(name__icontains= search_text)

            qs = qs.order_by("name")

            return qs

        except Exception as e:
            print("an exception occured : ",str(e))
            return TblMainLocations.objects.none()

    def put(self, request):

        try:

            obj_user = self.request.user
            user_validator = UserValidator(obj_user)

            id = request.data["id"]
            obj_mainlocation = TblMainLocations.objects.get(id= id)
            name = request.data["name"]
            is_active = request.data["is_Active"]
            print("request accepted")


            if user_validator.is_superuser == False:
                return JsonResponse(getValErrorDict("you are not identified as admin"))
            if name == "":
                return JsonResponse(getValErrorDict("invalid name"))
            if TblMainLocations.objects.filter(name__iexact= name).exclude(id= id).count() > 0:
                return JsonResponse(getValErrorDict("location already found in this name"))
            if is_active not in lst_string_bool_values_without_blank:
                return JsonResponse(getValErrorDict("Invalid value for 'is_active'"))
            is_active = get_bool_of_string(is_active)
            print("request validated")


            obj_mainlocation.name = name
            obj_mainlocation.is_active = is_active
            obj_mainlocation.save()
            print("main location updated")


            return JsonResponse(getSuccessDict("main location updated",{"id" : obj_mainlocation.id}))



        except Exception as e:
            return JsonResponse(getErrorDict("an error occured",str(e)))

    def delete(self, request):

        try:

            obj_user = self.request.user
            user_validator = UserValidator(obj_user)
            print("user recognition completed")

            id = request.GET["id"]
            obj_main_location = TblMainLocations.objects.get(id= id)
            print("request accepted")


            if user_validator.is_superuser == False:
                return JsonResponse(getValErrorDict("you don't have the permission"))
            print("request validated")

            obj_main_location.delete()
            print("deleted")

            return JsonResponse(getSuccessDict("deleted"))


        except Exception as e:
            return JsonResponse(getErrorDict("an error occured", str(e)))

