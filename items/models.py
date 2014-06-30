# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from profiles.models import UserProfile, GroupProfile
import datetime


class Tag(models.Model):
    slug = models.SlugField(verbose_name="Slug")

    def __unicode__(self):
        return self.slug

class Item(models.Model):
    active = models.BooleanField(verbose_name="Active", default=True)
    name = models.CharField(verbose_name="Name", max_length=128)
    description = models.TextField(verbose_name="Description")
    image = models.ImageField(upload_to="items/", blank=True, null=True)
    added_by = models.ForeignKey(User, related_name="added_by", verbose_name="Added by")
    rented_by = models.ForeignKey(User, related_name="rented_by", verbose_name="Rented by", blank=True, null=True)
    added_on = models.DateTimeField(verbose_name="Added on", editable=False, default=datetime.datetime.now)
    last_modified = models.DateTimeField(verbose_name="Modified on", editable=False, default=datetime.datetime.now)
    rented_on = models.DateTimeField(verbose_name="Rented On", blank=True, null=True)
    rented_to = models.DateTimeField(verbose_name="Rented To", blank=True, null=True)
    rent_power = models.SmallIntegerField(verbose_name="Rent Power", default=50, help_text=u"Power needed to rent item.")
    vision_power = models.SmallIntegerField(verbose_name="Vision Power", default=50, help_text=u"Power needed to view item.")
    tags = models.ManyToManyField(Tag, verbose_name="Tag")

    def __unicode__(self):
        return self.name

    def available(self):
        if self.rented_by:
            return False
        else:
            return True

    def tag_list(self):
        tags = self.tags.values_list("slug", flat=True)[:3]
        return ", ".join(tags)

    def added_on_date(self):
        return self.added_on.strftime("%Y-%m-%d %H:%M:%S")

    def save(self, *args, **kwargs):
        """
        Update timestamps on save action.
        """

        if not self.pk:
            self.added_on = datetime.datetime.now()
        self.last_modified = datetime.datetime.now()

        return super(Item, self).save(*args, **kwargs)
