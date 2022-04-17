from django.db import models

# Create your models here.

class TblMainLocations(models.Model):

    name = models.TextField(null= False,blank= False)
    is_active = models.BooleanField(null= False,blank= False,default= True)

