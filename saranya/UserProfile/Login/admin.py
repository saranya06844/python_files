from django.contrib import admin
from .models import UserDetails

class UserAdmin(admin.ModelAdmin):
    List = '__all__'

admin.site.register(UserDetails)


