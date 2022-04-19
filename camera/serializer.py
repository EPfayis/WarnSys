from .models import *
from WarnSys.Imports import *
from locations.serializer import MainLocationSerializer

class CameraSerializer(DynamicFieldsModelSerializer):

    location = MainLocationSerializer(many= False)

    class Meta:
        model = TblCamera
        fields = ["id","description","location"]

class CameraSerializerAdmin(DynamicFieldsModelSerializer):

    location = MainLocationSerializer(many= False)
    secret = serializers.SerializerMethodField()

    class Meta:
        model = TblCamera
        fields = ["id","description","secret","location"]

    def get_secret(self,data):
        print(data.id)
        objSecret = TblCamSecret.objects.get(camera_id = data.id)
        print(objSecret.id)
        return objSecret.code