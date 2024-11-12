from django.contrib import admin
from users.models import tbUsers
# Register your models here.


@admin.register(tbUsers)
class tbUsersAdmin(admin.ModelAdmin):
    list_display = ['email', 'nickname']