# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

# project imports
from utils.core.models import TimeStampable
from apps.accessories.models.company import Company

User = get_user_model()

class Stock(TimeStampable):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    buy_price = models.FloatField()
    
    def __str__(self):
        return self.name