from .models import *
from WarnSys.Imports import *
from locations.serializer import MainLocationSerializer
from camera.serializer import CameraSerializer
from picture.Serializer import TblImageSerializer

class AlertSerializer(DynamicFieldsModelSerializer):

    location = MainLocationSerializer(many=False)
    camera = CameraSerializer(many=False)
    image = TblImageSerializer(many=False)

    class Meta:
        model = TblAlert
        fields = ["id","date","camera","location","image"]
