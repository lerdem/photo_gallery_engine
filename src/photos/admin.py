from django.contrib import admin
from photos import models

admin.site.register(models.Photo)
admin.site.register(models.Tag)
admin.site.register(models.Voice)
admin.site.register(models.Comment)


