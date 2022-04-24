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

class MoneyTransfer(TimeStampable):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)