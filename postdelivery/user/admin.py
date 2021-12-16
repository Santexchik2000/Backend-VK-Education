from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from .models import UserProfile


class UserProfileAdmin(ModelAdmin):
    list_display = [
        "username", "get_full_name", "role"
    ]
    # list_display_links = ["login"]
    search_fields = ('role', 'username')
    
    list_filter = [
        "role"
    ]


admin.site.register(UserProfile, UserProfileAdmin)
