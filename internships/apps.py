# defines configuration for internshipfinder
# django uses, to know app name & setts

from django.apps import AppConfig

class InternshipfinderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'internships'
