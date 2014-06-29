# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import CharField, TextField, ManyToManyField, SlugField
from django.contrib.auth.models import User, Group

from profiles.models import UserProfile, GroupProfile


class Tag(models.Model):
    slug = SlugField(verbose_name="Slug")

    def __unicode__(self):
        return self.slug

class Item(models.Model):
    name = CharField(verbose_name="Name", max_length=128)
    description = TextField(verbose_name="Description")
    added_by = models.ForeignKey(User, related_name="added_by", verbose_name="Added by")
    rented_by = models.ForeignKey(User, related_name="rented_by", verbose_name="Rented by", blank=True, null=True)
    rent_power = models.SmallIntegerField(verbose_name="Rent Power", default=50, help_text=u"Power needed to rent item.")
    vision_power = models.SmallIntegerField(verbose_name="Vision Power", default=50, help_text=u"Power needed to view item.")
    tags = ManyToManyField(Tag, verbose_name="Tag")

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
