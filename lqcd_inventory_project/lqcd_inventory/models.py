from django.db import models


class DilutionScheme(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Ensemble(models.Model):
    mass_light = models.FloatField()

    def __str__(self):
        return r'\( \mu_l={} \)'.format(self.mass_light)

    def __repr__(self):
        return 'Ensemble({})'.format(repr(self.mass_light))


class Eigensystem(models.Model):
    path = models.CharField(max_length=1000)

    ensemble = models.ForeignKey(Ensemble, on_delete=models.CASCADE)

    def __str__(self):
        return '{} @ {}'.format(self.path, str(self.ensemble))


class Perambulator(models.Model):
    random_seed = models.IntegerField()
    mass_light = models.FloatField()
    mass_strange = models.FloatField()
    mass_charm = models.FloatField()

    ensemble = models.ForeignKey(Ensemble, on_delete=models.CASCADE)
    dilution_scheme = models.ForeignKey(DilutionScheme, on_delete=models.CASCADE, related_name='perambulators')

    def __str__(self):
        return 'mu_l={}, mu_s={}, mu_c={}'.format(self.mass_light, self.mass_strange, self.mass_charm)
