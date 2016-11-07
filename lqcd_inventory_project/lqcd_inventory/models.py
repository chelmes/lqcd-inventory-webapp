from django.db import models


class DilutionScheme(models.Model):
    name = models.CharField(max_length=200)


class Ensemble(models.Model):
    mu_l = models.FloatField()


class Eigensystem(models.Model):
    path = models.CharField(max_length=1000)

    ensemble = models.ForeignKey(Ensemble, on_delete=models.CASCADE)


class Perambulator(models.Model):
    random_seed = models.IntegerField()
    mass_light = models.FloatField()
    mass_strange = models.FloatField()
    mass_charm = models.FloatField()

    ensemble = models.ForeignKey(Ensemble, on_delete=models.CASCADE)
    dilution_scheme = models.ForeignKey(DilutionScheme, on_delete=models.CASCADE)

