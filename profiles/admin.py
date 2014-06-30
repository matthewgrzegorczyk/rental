from django.contrib import admin
from profiles.models import UserProfile, GroupProfile


class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    list_display = ['user', 'rent_power', 'vision_power']
    list_editable = ['rent_power', 'vision_power']


class GroupProfileAdmin(admin.ModelAdmin):
    model = GroupProfile
    list_display = ['group', 'rent_power', 'vision_power']
    list_editable = ['rent_power', 'vision_power']


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(GroupProfile, GroupProfileAdmin)
