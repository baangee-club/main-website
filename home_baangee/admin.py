from django.contrib import admin
from .models import (
    Programme,
    Guest,
    Message,
    Album,
    Photo,
    Article,
    Soach,
    Information,
    ContactPerson,
)


class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ["heading", "description", "album", "image1", "image2", "image3"]


class GuestAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]


class MessageAdmin(admin.ModelAdmin):
    list_display = ["message", "author"]


class PhotoAdmin(admin.ModelAdmin):
    list_display = ["image_tag", "album"]


class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "author"]


class SoachAdmin(admin.ModelAdmin):
    list_display = ["content"]


class InformationAdmin(admin.ModelAdmin):
    list_display = ["content"]


class ContactPersonAdmin(admin.ModelAdmin):
    list_display = ["name", "designation", "email", "mobile_number"]


admin.site.register(Programme, ProgrammeAdmin)
admin.site.register(Guest, GuestAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Album)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Soach, SoachAdmin)
admin.site.register(Information, InformationAdmin)
admin.site.register(ContactPerson, ContactPersonAdmin)
