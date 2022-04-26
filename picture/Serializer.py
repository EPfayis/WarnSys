from WarnSys.Imports import *
from .models import TblImage


class TblImageSerializer(DynamicFieldsModelSerializer):

    class Meta:

        model = TblImage
        fields = ["id","image"]