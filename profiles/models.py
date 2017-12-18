# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    # auth related information about the user (username, password, email, first_name, last_name)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # non-auth related information about the user
    description = models.CharField(max_length=255)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    nationality = models.CharField(max_length=20)
    passport_number = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    image = models.ImageField()
    ROLE_CHOICES = (
        ('host', 'Host'),
        ('guest', 'Guest'),
    )
    role = models.CharField(max_length=5, choices=ROLE_CHOICES)