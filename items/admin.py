from django.contrib import admin
from items.models import UserProfile, GroupProfile, Tag, Item

class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile

class ItemAdmin(admin.ModelAdmin):
    model = Item
    list_display = ['name', 'added_by', 'rented_by', 'rent_power', 'vision_power']
    list_editable = ['rented_by', 'rent_power', 'vision_power']

admin.site.register(UserProfile)
admin.site.register(GroupProfile)
admin.site.register(Tag)
admin.site.register(Item, ItemAdmin)
