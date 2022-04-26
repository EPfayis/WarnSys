from datetime import datetime

from django.shortcuts import render
from .models import TblAlert
from camera.models import TblCamera,TblCamSecret
from WarnSys.Imports import *
from picture.views import saveImageFromArray
from .serializer import AlertSerializer

# Create your views here.

class ClsAlert(ListAPIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    serializer_class = AlertSerializer

    def post(self, request):
        try:
            objUser = self.request.user
            userValidator = UserValidator(objUser)
            print("User Identified")

            date = datetime.now()
            camera = request.data["camera"]
            objCamera = TblCamera.objects.get(id=camera)
            objLocation = objCamera.location
            camSecret = request.data["camSecret"]
            image = request.FILES["image"]
            print("Request Accepted")

            camSec = TblCamSecret.objects.get(camera=objCamera).code
            if camSec != camSecret:
                return JsonResponse(getValErrorDict("Camera authentication failed"))
            print("Request validated")

            objImage = saveImageFromArray([image])[0]

            objAlert = TblAlert()
            objAlert.date = date
            objAlert.camera = objCamera
            objAlert.location = objLocation
            objAlert.image = objImage
            objAlert.save()
            print("Alert saved")

            return JsonResponse(getSuccessDict("Alert saved"))

        except Exception as e:
            print("Exception occurred :", str(e))
            return JsonResponse(getErrorDict("An error occurred", str(e)))

    def get_queryset(self):
        try:
            objUser = self.request.user
            userValidator = UserValidator(objUser)
            print("User Identified")

            searchText = self.request.GET.get("searchText","")
            fromDate = self.request.GET.get("fromDate","")

            toDate = self.request.GET.get("toDate","")

            print("Request accepted")

            qs = TblAlert.objects.all().order_by("date")

            if fromDate != "":
                fromDate = datetime.strptime(fromDate, DATE_TIME_FORMAT)
                qs = qs.exclude(date__lt= fromDate)
            if toDate != "":
                toDate = datetime.strptime(toDate, DATE_TIME_FORMAT)
                qs = qs.exclude(date__gt= toDate)

            qs = qs.filter(Q(location__name__icontains=searchText) | Q(camera__description__icontains=searchText))

            return qs

        except Exception as e:
            print("An error occurred : ", str(e))
            return TblAlert.objects.none()