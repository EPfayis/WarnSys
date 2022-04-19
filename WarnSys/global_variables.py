
'''Declaring some Global Variable'''
import sys


MESSAGE = "Message"
ERROR = "Error"
STATUS = "Status"
DELIVERY_BOY = "delivery_boy"
ORDER_MANAGEMENT = "order_management"
STOCK_MANAGEMENT = "stock_management"



def generateId(key,value):
    n = value # will be the last id from table
    str = key # will be the Preceding Word
    id = str+f'{n:05}'
    print("Generated id : ",id)
    return  id


import random
import string

def get_random_alphaNumeric_string(stringLength=8):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))



def getErrorDict(message,error):
    d = {
        MESSAGE : message,
        ERROR : error,
        STATUS : False
    }
    return d

def getSuccessDict(message,additional = {}):
    d = {
        MESSAGE : message,
        STATUS : True
    }
    d.update(additional)
    return d

def getValErrorDict(message, additional = {}):
    d = {
        MESSAGE: "Validation error occured",
        ERROR : message,
        STATUS: False
    }
    d.update(additional)
    return d


lst_string_bool_values_without_blank = ["true", "false", "0", "1", True, False]
lst_string_bool_values_with_blank =    ["true", "false", "0", "1", True, False, ""]

def get_bool_of_string(value):
    if value == True:
        return True
    if value == False:
        return False
    if value == "":
        return ""
    if value == "true":
        return True
    if value == "false":
        return False
    if value == "0":
        return False
    if value == "1":
        return True


def getFloatOfObject(obj):

    try:
        return float(obj)
    except:
        return 0


def blankValidator(lst_values):

    for i in lst_values:
        if i["value"] == "":
            return "invalid " + str(i["var"])
    return True