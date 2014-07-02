# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import CharField, TextField, ManyToManyField, SlugField
from django.contrib.auth.models import User, Group
from django.core.urlresolvers import reverse

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    image = models.ImageField(verbose_name="User Avatar", upload_to="users/", blank=True, null=True)
    rent_power = models.SmallIntegerField(verbose_name=u"Rent Power", default=50, help_text=u"Power needed to rent item.")
    vision_power = models.SmallIntegerField(verbose_name=u"Vision Power", default=50, help_text=u"Power needed to view item.")

    def __unicode__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('profiles.views.view_user', args=[str(self.pk)])


class GroupProfile(models.Model):
    group = models.OneToOneField(Group)
    description = models.TextField(blank=True)
    rent_power = models.SmallIntegerField(verbose_name=u"Rent Power", default=50, help_text=u"Power needed to rent item.")
    vision_power = models.SmallIntegerField(verbose_name=u"Vision Power", default=50, help_text=u"Power needed to view item.")

    def __unicode__(self):
        return self.group.name
