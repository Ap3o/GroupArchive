from django.contrib import admin

from .models import Gallery, Group


@admin.register(Gallery)
class AdminGallery(admin.ModelAdmin):
    list_display = ('group', 'photo', 'description')


@admin.register(Group)
class AdminGroup(admin.ModelAdmin):
    list_display = ('name',)
