from .models import *
from chatfood.Imports import *
from company.models import TblBranch
from users.serializers import UserSerializer

class MainLocationSerializerSimple(DynamicFieldsModelSerializer):

    class Meta:
        model = TblMainLocations
        fields = ["id","name"]


class SubLocationSerializer(DynamicFieldsModelSerializer):

    parent_location = MainLocationSerializerSimple(many= False)

    class Meta:
        model = TblSubLocations
        fields = "__all__"


class MainLocationSerializer(DynamicFieldsModelSerializer):

    sub_locations = serializers.SerializerMethodField()

    class Meta:
        model = TblMainLocations
        fields = ["id","name","sub_locations"]

    def get_sub_locations(self,obj):

        # company_name = self.context['request'].GET.get("company_name","")
        # qs_branch = TblBranch.objects.filter()

        lst_sub_loc = self.context["request"].data.get("lst_sub_loc",[])

        qs = TblSubLocations.objects.filter(parent_location= obj)
        qs = qs.filter(id__in= lst_sub_loc)
        sr = SubLocationSerializer(qs,many= True,exclude=["parent_location"])
        return sr.data
