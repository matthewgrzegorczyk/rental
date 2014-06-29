# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import CharField, TextField, ManyToManyField, SlugField
from django.contrib.auth.models import User, Group


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    rent_power = models.SmallIntegerField(verbose_name=u"Rent Power", default=50, help_text=u"Power needed to rent item.")
    vision_power = models.SmallIntegerField(verbose_name=u"Vision Power", default=50, help_text=u"Power needed to view item.")

    def __unicode__(self):
        return self.user.username

class GroupProfile(models.Model):
    group = models.OneToOneField(Group)
    description = models.TextField(blank=True)
    rent_power = models.SmallIntegerField(verbose_name=u"Rent Power", default=50, help_text=u"Power needed to rent item.")
    vision_power = models.SmallIntegerField(verbose_name=u"Vision Power", default=50, help_text=u"Power needed to view item.")

    def __unicode__(self):
        return self.group.name
