from django.contrib import admin
from .models import Inventory

#Create a class for display on WebPage
class InventoryAdmin(admin.ModelAdmin):
    list_display = ("title", "quantity", "price", "status")

# Register your models here.
admin.site.register(Inventory, InventoryAdmin)