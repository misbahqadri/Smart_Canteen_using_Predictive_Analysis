from django.contrib import admin
from .models import ngos

# Register your models here.
@admin.register(ngos)
class ngosadmin(admin.ModelAdmin):
    pass