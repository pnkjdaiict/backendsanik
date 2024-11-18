from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.
admin.site.register(State)
admin.site.register(Cities)

