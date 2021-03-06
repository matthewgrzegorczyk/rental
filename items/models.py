# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from profiles.models import UserProfile, GroupProfile
import datetime


class Tag(models.Model):
    slug = models.SlugField(verbose_name="Slug")

    def __unicode__(self):
        return self.slug


class ItemManager(models.Manager):
    def get_queryset(self):
        return super(ItemManager, self).get_queryset().filter(active=True, vision_power__lte=settings.VISION_POWER)


class Item(models.Model):
    """
    Basic item model.

    Usage:
    item = Item.objects.get(pk=id)
    user = item.added_by

    # Get user rented items
    rented_items = user.items_rented.all()

    # Get user items added by user
    user_items = user.items_added.all()
    """

    active = models.BooleanField(verbose_name="Active", default=True)
    name = models.CharField(verbose_name="Name", max_length=128)
    description = models.TextField(verbose_name="Description")
    image = models.ImageField(verbose_name="Image", upload_to="items/", blank=True, null=True)
    added_by = models.ForeignKey(User, related_name="items_added", verbose_name="Added by")
    rented_by = models.ForeignKey(User, related_name="items_rented", verbose_name="Rented by", blank=True, null=True)
    added_on = models.DateTimeField(verbose_name="Added on", editable=False, default=datetime.datetime.now)
    last_modified = models.DateTimeField(verbose_name="Modified on", editable=False, default=datetime.datetime.now)
    rented_on = models.DateTimeField(verbose_name="Rented on", blank=True, null=True)
    rented_to = models.DateTimeField(verbose_name="Rented to", blank=True, null=True)
    rent_power = models.SmallIntegerField(verbose_name="Rent Power", default=settings.RENT_POWER, help_text=u"Power needed to rent item.")
    vision_power = models.SmallIntegerField(verbose_name="Vision Power", default=settings.VISION_POWER, help_text=u"Power needed to view item.")
    tags = models.ManyToManyField(Tag, verbose_name="Tag")

    objects = models.Manager()
    published = ItemManager()

    class Meta:
        get_latest_by = "added_on"
        ordering = ['-added_on', '-last_modified']

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
