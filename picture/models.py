from django.db import models

# Create your models here.


class TblImage(models.Model):
    image = models.FileField(blank= False,null= False)