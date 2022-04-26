from django.http import HttpResponse
from django.shortcuts import render
from .Serializer import TblImageSerializer
from .models import TblImage
from WarnSys.settings import BASE_DIR
from WarnSys.settings import MEDIA_URL
import os
from WarnSys.Imports import getContentTypeObject
from WarnSys.Imports import getContentTypePath
# Create your views here.


def saveImageFromArray(lst_image):

    lst_output = []

    for image in lst_image:

        if image == None:
            lst_output.append(None)
            continue
        if image == "null":
            lst_output.append(None)
            continue

        type = getContentTypeObject(image)
        flag = type.find("image",0,len(type) - 1)
        if flag == -1:
            lst_output.append(None)
            print("file rejected")
            continue


        obj_image = TblImage()
        obj_image.image = image
        obj_image.save()
        lst_output.append(obj_image)

    return lst_output



def imageHandler(request,file_name):

    path = BASE_DIR + MEDIA_URL + file_name
    obj_image = open(path, 'rb')
    content_type = getContentTypePath(path)
    return HttpResponse(obj_image, content_type= content_type)

