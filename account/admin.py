from django.contrib import admin
from .models import UserProfile
from django.utils.html import mark_safe

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio', 'display_profile_picture']
    list_filter = ['user']
    search_fields = ['user', 'bio']

    def display_profile_picture(self, obj):
        if obj.profile_picture:
            return mark_safe(f'<img src="{obj.profile_picture.url}" style="width: 50px; height: 50px; border-radius: 50%;">')
        else:
            return 'No Image'

    display_profile_picture.short_description = 'Profile Picture'

admin.site.register(UserProfile, UserProfileAdmin)