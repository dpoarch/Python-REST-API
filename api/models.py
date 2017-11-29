# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from uuid import uuid4

def generateUUID():
    return str(uuid4())

# Create your models here.

class risk_type(models.Model):
   
    name = models.CharField(max_length=100, blank=False, unique=False)

    def __str__(self):
        return "{}".format(self.name)

class risk_type_fields(models.Model):
    """This class represents the bucketlist model."""
    risk_type_id = models.CharField(max_length=100, blank=False, unique=False)
    fieldname = models.CharField(max_length=100, blank=False, unique=False)
    fieldtype = models.CharField(max_length=100, blank=False, unique=False)

    def __str__(self):
        return "{}".format(self.fieldname)