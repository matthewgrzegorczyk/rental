# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import CharField, TextField, ManyToManyField, SlugField
from django.contrib.auth.models import User, Group
from django.core.urlresolvers import reverse

from django.utils import timezone


class UserProfile(models.Model):
    """
    Extending user model with some extra fields to make app more cool.
    """

    user = models.OneToOneField(User)
    image = models.ImageField(verbose_name="User Avatar", upload_to="users/", blank=True, null=True)
    description = models.TextField(blank=True)
    rent_power = models.SmallIntegerField(verbose_name=u"Rent Power", default=50, help_text=u"Power needed to rent item.")
    vision_power = models.SmallIntegerField(verbose_name=u"Vision Power", default=50, help_text=u"Power needed to view item.")

    def __unicode__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('profiles.views.view_user', args=[str(self.user.username)])

    def rent_item(self, item, date_to):
        """
        Rent item by user.

        :param item: Item object.
        :type item: Item.
        :param date_to: Date to item is rent.
        :type date_to: datetime.
        :returns: True if item is rented successfully or False if not.
        :rtype: Boolean.
        """

        if self.rent_power >= item.rent_power:
            item.rented_by = self.user
            item.rented_on = timezone.now()
            item.rented_to = date_to
            item.save()
            return True

        return False


class GroupProfile(models.Model):
    group = models.OneToOneField(Group)
    description = models.TextField(blank=True)
    rent_power = models.SmallIntegerField(verbose_name=u"Rent Power", default=50, help_text=u"Power needed to rent item.")
    vision_power = models.SmallIntegerField(verbose_name=u"Vision Power", default=50, help_text=u"Power needed to view item.")

    def __unicode__(self):
        return self.group.name

    def get_absolute_url(self):
        return reverse('profiles.view.view_group', args=[str(self.group.name)])
