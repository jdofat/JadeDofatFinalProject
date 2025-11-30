# tracks the internships

from django.db import models

class Internship(models.Model):
# internship model
    # title of int, comp name, location of job, description & url
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        # shows title
        return self.title
