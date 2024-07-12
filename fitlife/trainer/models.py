from django.db import models
from django.conf import settings
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import AbstractUser,Group, Permission


class Trainer(models.Model):
    GENDER_CHOICES = [
        ('erkek', 'Erkek'),
        ('kadin', 'Kadin'),
        ('diger', 'Diger'),
    ]

    SPECIALIZATION_CHOICES = [
        ('kilo_alma', 'Kilo Alma'),
        ('kilo_verme', 'Kilo Verme'),
        ('kilo_koruma', 'Kilo Koruma'),
        ('kas_kazanma', 'Kas Kazanma'),
    ]
    ##user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='trainer_profile', default=None)
    trainer_email = models.EmailField(unique=True)
    trainer_password = models.CharField(max_length=128,default='123456')
    trainer_first_name = models.CharField(max_length=30)
    trainer_last_name = models.CharField(max_length=30)
    trainer_birthdate = models.DateField(default=timezone.now)
    trainer_gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    trainer_uzmanlık = models.CharField(max_length=20, choices=SPECIALIZATION_CHOICES)
    trainer_experiences = models.TextField()
    trainer_kont = models.PositiveIntegerField(default=5)
    trainer_phone_number = models.CharField(max_length=15)
    USERNAME_FIELD = 'trainer_email'
    groups = models.ManyToManyField(Group, related_name='trainer_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='trainer_permissions')
    

