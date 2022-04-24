# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

# project imports
from utils.core.models import TimeStampable

User = get_user_model()

class Earning(TimeStampable):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    buy_price = models.IntegerField()
    sold_price = models.IntegerField()
    
    @property
    def earning(self):
        return self.sold_price - self.buy_price
    
    def __str__(self):
        return self.name