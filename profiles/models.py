# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    # auth related information about the user (username, password, email, first_name, last_name)
    # on_delete=models.CASCADE Automatically deletes related records when the related instance is removed
    user = models.OneToOneField(User, on_delete=models.CASCADE) # extend default Djando User model using a One-To-One Link

    # non-auth related information about the user
    picture = models.FileField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    nationality = models.CharField(max_length=100)
    passport_number = models.CharField(max_length=20)
    passport_file = models.ImageField()
    ROLE_CHOICES = (
        ('host', 'Host'),
        ('guest', 'Guest'),
    )
    role = models.CharField(max_length=5, choices=ROLE_CHOICES, default='guest')
    phone_number = models.CharField(max_length=20)
    description = models.CharField(max_length=200)