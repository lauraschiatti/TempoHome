# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    address = models.CharField(max_length=150)
    description = models.CharField(max_length=200)
    rules = models.CharField(max_length=200, blank=True)
    user = models.ForeignKey(User)

class Picture(models.Model):
    picture = models.ImageField()
    room = models.ForeignKey(Room)

class Request(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    user = models.ForeignKey(User)
    room = models.ForeignKey(Room)
    STATUS_CHOICES = (
        ('P', 'Pending'),
        ('A', 'Approved'),
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    comments = models.CharField(max_length=250, blank=True)