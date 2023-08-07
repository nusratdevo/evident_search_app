from django.contrib import admin
from .models import CustomUser, SortedInput

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list = ('name', 'email','username')

    admin.site.register(CustomUser)
    
class SortedInputAdmin(admin.ModelAdmin):
    list = ('input_values', 'search_value', 'timestamp')

    admin.site.register(SortedInput)