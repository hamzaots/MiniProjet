from django.contrib import admin

# Register your models here.
from .models import dateasyn

class DateAdmin(admin.ModelAdmin):
    list_display = ('ip_address','scan_type','start_time')

admin.site.register(dateasyn,DateAdmin)