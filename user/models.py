from django.db import models
from django.contrib.auth.models import User
from locations.models import TblMainLocations

# Create your models here.

class TblUserDetails(models.Model):
    user = models.ForeignKey(User, null= False,blank= False,on_delete= models.CASCADE)
    mobile = models.TextField(null= False, blank= False)
    warnLocations = models.ManyToManyField(TblMainLocations)

