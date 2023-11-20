from django.contrib import admin

from . import models
from .models import Profileinfo1, Profileinfolocationbd, Profileinfolocationabroad, Profileinfoexperience,Profilecomplete1, Profilecomplete2, Profilecomplete3, Profilecomplete4, Profilecomplete5

class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "firstname")


admin.site.register(models.User, UserAdmin)



@admin.register(Profileinfo1)
class Profileinfo1Admin(admin.ModelAdmin):
    list_display = ('user', 'user_name', 'gender', 'date_of_birth')

@admin.register(Profileinfolocationbd)
class ProfileinfolocationbdAdmin(admin.ModelAdmin):
    list_display = ('user', 'District')

@admin.register(Profileinfolocationabroad)
class ProfileinfolocationabroadAdmin(admin.ModelAdmin):
    list_display = ('user', 'countryname', 'city', 'duration')

@admin.register(Profileinfoexperience)
class ProfileinfoexperienceAdmin(admin.ModelAdmin):
    list_display = ('user', 'industry', 'areaofexpertise', 'durationstay')



admin.site.register(Profilecomplete1)
admin.site.register(Profilecomplete2)
admin.site.register(Profilecomplete3)
admin.site.register(Profilecomplete4)
admin.site.register(Profilecomplete5)