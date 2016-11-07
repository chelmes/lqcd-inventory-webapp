from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from . import models


def index(request):
    return render(request, 'lqcd_inventory/index.html')


def perambulators_index(request):
    perambulator_list = models.Perambulator.objects.order_by('random_seed')

    return render(
        request,
        'lqcd_inventory/perambulators_index.html',
        {
            'perambulator_list': perambulator_list,
        },
    )


def perambulators_create(request):
    return render(request, 'lqcd_inventory/404.html')


class PerambulatorView(generic.DetailView):
    model = models.Perambulator
    template_name = 'lqcd_inventory/perambulators_view.html'


class DilutionSchemeView(generic.DetailView):
    model = models.DilutionScheme
    template_name = 'lqcd_inventory/dilution_schemes_view.html'


class EnsembleView(generic.DetailView):
    model = models.Ensemble
    template_name = 'lqcd_inventory/ensembles_view.html'
