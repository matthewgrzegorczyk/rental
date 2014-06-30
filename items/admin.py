from django.contrib import admin
from items.models import UserProfile, GroupProfile, Tag, Item

class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    list_display = ['user', 'rent_power', 'vision_power']
    list_editable = ['rent_power', 'vision_power']

class GroupProfileAdmin(admin.ModelAdmin):
    model = GroupProfile
    list_display = ['group', 'rent_power', 'vision_power']

class ItemAdmin(admin.ModelAdmin):
    model = Item
    list_display = ['active', 'name', 'added_by', 'added_on', 'rented_by', 'rented_on', 'rent_power', 'vision_power', 'tag_list', 'last_modified']
    list_display_links = ['name']
    list_editable = ['rented_by', 'rent_power', 'vision_power']
    filter_horizontal = ['tags']
    fieldsets = (
        ('Basic item info', {
            'fields': (('name', 'active'), 'description', 'image', 'added_by', 'rented_by')
        }),
        ('Permissions', {
            'fields': ('rent_power', 'vision_power')
        }),
        ('Additional Info', {
            'fields': ('tags',)
        }),
    )


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(GroupProfile)
admin.site.register(Tag)
admin.site.register(Item, ItemAdmin)
