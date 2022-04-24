# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.db.models import TextChoices

# project imports
from utils.core.models import TimeStampable
from apps.recharge.models import Company, Plan

User = get_user_model()

class MNP(TimeStampable):

    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    price = models.IntegerField()
    
    def __str__(self):
        return self.name