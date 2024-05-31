from django.contrib import admin
from .models import shallvhack
# Register your models here.
@admin.register(shallvhack)
class shallvhackModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc']
    
