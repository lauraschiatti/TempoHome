# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    address = models.CharField(max_length=150)
    description = models.CharField(max_length=200)
    rules = models.CharField(max_length=200, blank=True)
    STATUS_CHOICES = (
        ('F', 'Free'),
        ('O', 'Occupied'),
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='F')
    user = models.ForeignKey(User)


class Picture(models.Model):
    picture = models.ImageField()
    room = models.ForeignKey(Room)
