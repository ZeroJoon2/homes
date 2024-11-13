from django.contrib import admin
from demand.models import tbDemands
# Register your models here.

@admin.register(tbDemands)
class tbDemandAdmin(admin.ModelAdmin):
    list_display = ['id', 'post_title','email', 'image1', 'image2', 'image3']
    pass