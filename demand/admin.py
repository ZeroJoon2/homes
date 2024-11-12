from django.contrib import admin
from demand.models import tbDemands
# Register your models here.

@admin.register(tbDemands)
class tbDemandAdmin(admin.ModelAdmin):
    list_display = ['id', 'post_title','email']
    pass