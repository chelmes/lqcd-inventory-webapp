from django.contrib import admin

from . import models

admin.site.register(models.Dilution)
admin.site.register(models.Eigensystem)
admin.site.register(models.Ensemble)
admin.site.register(models.Perambulator)
admin.site.register(models.PerambulatorSeed)
admin.site.register(models.Storage)
