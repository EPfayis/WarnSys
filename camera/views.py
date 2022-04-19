from django.shortcuts import render
from WarnSys.Imports import *
from locations.models import *
from .models import *
from .serializer import *

class ClsCamera(ListAPIView):

    serializer_class = CameraSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def post(self,request):
        lstObjects = []
        try:

            objUser = self.request.user
            userValidator = UserValidator(objUser)
            print("User Identified")

            location = request.data["location"]
            objLocation = TblMainLocations.objects.get(id= location)
            description = request.data["description"]
            print("Request accepted")

            if userValidator.is_superuser == False:
                return JsonResponse(getValErrorDict("You are not an admin"))
            if objLocation.is_active == False:
                return JsonResponse(getValErrorDict("This location is not active"))
            print("Request validated")

            objCamera = TblCamera()
            objCamera.location = objLocation
            objCamera.description = description
            objCamera.save()
            lstObjects.append(objCamera)
            print("Camera saved")

            rand = get_random_alphaNumeric_string(8)

            objCamSecret = TblCamSecret()
            objCamSecret.camera = objCamera
            objCamSecret.code = rand
            objCamSecret.save()
            lstObjects.append(objCamSecret)
            print("Camera secret saved")

            return JsonResponse(getSuccessDict("Camera details saved"))

        except Exception as e:
            print("Exception occurred :", str(e))
            for i in reversed(lstObjects):
                i.delete()
            return JsonResponse(getErrorDict("An error occurred", str(e)))

    def get_queryset(self):
        try:
            objUser = self.request.user
            userValidator = UserValidator(objUser)

            if(userValidator.is_superuser == True):
                self.serializer_class = CameraSerializerAdmin

            searchText = self.request.GET.get("searchText","")

            qs = TblCamera.objects.all()
            qs = qs.filter(Q(location__name__icontains=searchText) | Q(description__icontains=searchText))
            return qs

        except Exception as e:
            print("An error occurred : ", str(e))
            return TblCamera.objects.none()
