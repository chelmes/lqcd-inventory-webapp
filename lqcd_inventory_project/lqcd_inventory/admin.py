from django.contrib import admin

from . import models

admin.site.register(models.DilutionScheme)
admin.site.register(models.Eigensystem)
admin.site.register(models.Ensemble)
admin.site.register(models.Perambulator)
