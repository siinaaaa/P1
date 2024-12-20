from django.contrib import admin
from .models import ImageProcessing


# Register your models here.

@admin.register(ImageProcessing)
class ImageProcessingAdmin(admin.ModelAdmin):
    list_display = ['unique_code']
    search_fields = ('unique_code',)
    list_per_page = 10
