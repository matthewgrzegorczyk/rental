from django.contrib import admin
from django.db import models
from items.models import UserProfile, GroupProfile, Tag, Item


def unrent_items(modeladmin, request, queryset):
    queryset.update(rented_by=None)
unrent_items.short_description = "Unset rented by"


def make_published(modeladmin, request, queryset):
    queryset.update(active=True)
make_published.short_description = "Make items active"


def make_unpublished(modeladmin, request, queryset):
    queryset.update(active=False)
make_unpublished.short_description = "Make items not active"


class ItemAdmin(admin.ModelAdmin):
    model = Item

    actions = [unrent_items, make_published, make_unpublished]
    filter_horizontal = ['tags']
    fieldsets = (
        ('Basic item info', {
            'fields': (('name', 'active'), 'description', 'image', 'added_by')
        }),
        ('Renting information', {
            'fields': ('rented_by', 'rented_on', 'rented_to')
        }),
        ('Permissions', {
            'fields': ('rent_power', 'vision_power')
        }),
        ('Additional Info', {
            'fields': ('tags',)
        }),
    )
    list_display = ['active', 'name', 'added_by', 'added_on', 'rented_by', 'rented_on', 'rent_power', 'vision_power', 'tag_list', 'last_modified']
    list_display_links = ['name']
    list_editable = ['rented_by', 'rent_power', 'vision_power']
    list_filter = ['active', 'added_by', 'rented_by', 'added_on', 'rented_on', 'last_modified', 'tags']



# admin.site.register(UserProfile, UserProfileAdmin)
# admin.site.register(GroupProfile)
admin.site.register(Tag)
admin.site.register(Item, ItemAdmin)
