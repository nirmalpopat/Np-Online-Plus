# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

# project imports
from utils.core.models import TimeStampable
from apps.sim.models.company import Company

User = get_user_model()

class Plan(TimeStampable):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    insentive_in_activation = models.FloatField()
    insentive_in_mnp = models.FloatField()
    
    def __str__(self):
        return self.name