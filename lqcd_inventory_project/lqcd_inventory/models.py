from django.db import models


class DilutionScheme(models.Model):
    name = models.CharField(max_length=200)
    letter = models.CharField(max_length=5)
    value = models.IntegerField()

    def __str__(self):
        return '{}.{}'.format(letter, value)


class Ensemble(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def __repr__(self):
        return 'Ensemble({})'.format(repr(self.name))


class Storage(models.Model):
    name = models.CharField(max_length=1000)
    account = models.CharField(max_length=1000, null=True)
    path = models.CharField(max_length=1000)


class Eigensystem(models.Model):
    path = models.CharField(max_length=1000)

    hyp_strength1 = models.FloatField()
    hyp_strength2 = models.FloatField()
    hyp_iterations = models.IntegerField()

    eigenvector_count = models.IntegerField()

    ev_ts_lambda_c = models.FloatField()
    ev_ts_lambda_l = models.FloatField()

    config_start = models.IntegerField()
    config_end = models.IntegerField()
    config_step = models.IntegerField()

    storage = models.ForeignKey(Storage, on_delete=models.CASCADE, related_name='eigensystem')

    @property
    def total_number(self):
        return (self.config_end - self.config_start) / self.config_step + 1

    ensemble = models.ForeignKey(Ensemble, on_delete=models.CASCADE, related_name='eigensystems')

    comment = models.CharField(max_length=2000, null=True)

    def __str__(self):
        return '{} @ {}'.format(self.path, str(self.ensemble))


class Perambulator(models.Model):
    mass_light = models.FloatField()
    mass_strange = models.FloatField()
    mass_charm = models.FloatField()

    dilution_source_time = models.ForeignKey(DilutionScheme, on_delete=models.CASCADE, related_name='perambulator_source_time')
    dilution_source_space = models.ForeignKey(DilutionScheme, on_delete=models.CASCADE, related_name='perambulator_source_space')
    dilution_source_laph = models.ForeignKey(DilutionScheme, on_delete=models.CASCADE, related_name='perambulator_source_laph')
    dilution_source_dirac = models.ForeignKey(DilutionScheme, on_delete=models.CASCADE, related_name='perambulator_source_dirac')

    dilution_sink_time = models.ForeignKey(DilutionScheme, on_delete=models.CASCADE, related_name='perambulator_sink_time')
    dilution_sink_space = models.ForeignKey(DilutionScheme, on_delete=models.CASCADE, related_name='perambulator_sink_space')
    dilution_sink_laph = models.ForeignKey(DilutionScheme, on_delete=models.CASCADE, related_name='perambulator_sink_laph')
    dilution_sink_dirac = models.ForeignKey(DilutionScheme, on_delete=models.CASCADE, related_name='perambulator_sink_dirac')

    ensemble = models.ForeignKey(Ensemble, on_delete=models.CASCADE, related_name='perambulators')

    storage = models.ForeignKey(Storage, on_delete=models.CASCADE, related_name='perambulator')

    comment = models.CharField(max_length=2000, null=True)

    def __str__(self):
        return 'mu_l={}, mu_s={}, mu_c={}'.format(self.mass_light, self.mass_strange, self.mass_charm)


class PerambulatorSeed(models.Model):
    seed_id = models.IntegerField()
    seed = models.IntegerField()
    perambulator = models.ForeignKey(Perambulator, on_delete=models.CASCADE, related_name='perambulator_seed')

