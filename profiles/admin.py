from django.contrib import admin

from .models import Profile


class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, PostAdmin)
