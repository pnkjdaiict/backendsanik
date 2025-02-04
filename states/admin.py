from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.
class CitiesAdmin(admin.ModelAdmin):
    list_filter = ('state',) 
    show_full_result_count = True
     # Enables filtering by course
class LocalitiesAdmin(admin.ModelAdmin):
    list_filter = ('city',) 
    show_full_result_count = True  

admin.site.register(State)
admin.site.register(Cities,CitiesAdmin)
admin.site.register(Localities,LocalitiesAdmin)
