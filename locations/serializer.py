from .models import *
from WarnSys.Imports import *


class MainLocationSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = TblMainLocations
        fields = ["id","name"]

