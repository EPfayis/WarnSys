from django.db import models
from locations.models import TblMainLocations
from picture.models import TblImage
from camera.models import TblCamera

class TblAlert(models.Model):
    date = models.DateTimeField(null=False, blank=False)
    location = models.ForeignKey(TblMainLocations, null=False, blank=False, on_delete=models.CASCADE)
    image = models.ForeignKey(TblImage, null=False, blank=False, on_delete=models.CASCADE)
    camera = models.ForeignKey(TblCamera, null=False, blank=False, on_delete=models.CASCADE)
