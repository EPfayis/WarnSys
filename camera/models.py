from django.db import models
from locations.models import TblMainLocations

# Create your models here.

class TblCamera(models.Model):
    location = models.ForeignKey(TblMainLocations, null=False, blank=False, on_delete=models.PROTECT)
    description = models.TextField(null=False, default="")

class TblCamSecret(models.Model):
    camera = models.OneToOneField(TblCamera, null=False, blank=False, on_delete=models.CASCADE)
    code = models.TextField(null= False, blank=False)