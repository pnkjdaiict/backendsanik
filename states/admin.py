from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.
 
class LocalitiesAdmin(admin.ModelAdmin):
    list_filter = ('city',) 
    show_full_result_count = True  

class CitiesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'state')  # Add any other fields you want to display

admin.site.register(Cities, CitiesAdmin)
admin.site.register(State)
 
admin.site.register(Localities,LocalitiesAdmin)
