from django.contrib import admin
from items.models import UserProfile, GroupProfile, Tag, Item

class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    list_display = ['user', 'rent_power', 'vision_power']
    list_editable = ['rent_power', 'vision_power']

class ItemAdmin(admin.ModelAdmin):
    model = Item
    list_display = ['name', 'added_by', 'added_on_date', 'rented_by', 'rented_on', 'rent_power', 'vision_power', 'tag_list']
    list_editable = ['rented_by', 'rent_power', 'vision_power']


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(GroupProfile)
admin.site.register(Tag)
admin.site.register(Item, ItemAdmin)
