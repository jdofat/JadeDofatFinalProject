# controls how internship items look in the admin view

from django.contrib import admin
from .models import Internship

class InternshipAdmin(admin.ModelAdmin):
    list_display = ["title", "company", "location"]
    # list_display shows columns
admin.site.register(Internship, InternshipAdmin)
