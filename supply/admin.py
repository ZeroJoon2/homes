from django.contrib import admin
from .models import tbSupply, PropertyListing


@admin.register(tbSupply)
class PropertyListingAdmin(admin.ModelAdmin):
    list_display = ['email', 'post_title', 'house_type_name', 'house_transaction_name', 'house_location_name']
    pass

@admin.register(PropertyListing)
class PropertyListingAdmin(admin.ModelAdmin):
    list_display = ['email', 'image1']
    pass