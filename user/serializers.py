from django.contrib.auth.models import User
from rest_framework import serializers, exceptions
from .models import *
from WarnSys.Imports import *
from locations.serializer import MainLocationSerializer



class UserDetailsSerializers(DynamicFieldsModelSerializer):

    warnLocations = MainLocationSerializer(many= True,read_only= True)

    class Meta:
        model = TblUserDetails
        fields = ["mobile","warnLocations"]


class UserSerializer(DynamicFieldsModelSerializer):

    details = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id","first_name","username","email","details",]

    def get_details(self,obj):
        qs = TblUserDetails.objects.filter(user= obj)
        if qs.count() == 0:
            return None
        sr = UserDetailsSerializers(qs.first(),many= False)
        return sr.data


