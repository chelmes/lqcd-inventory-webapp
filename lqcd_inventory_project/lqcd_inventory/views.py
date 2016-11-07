from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from . import models


def index(request):
    return render(request, 'lqcd_inventory/index.html')


class PerambulatorList(generic.ListView):
    model = models.Perambulator
    template_name = 'lqcd_inventory/perambulator_list.html'


def perambulators_create(request):
    return render(request, 'lqcd_inventory/404.html')


class PerambulatorView(generic.DetailView):
    model = models.Perambulator
    template_name = 'lqcd_inventory/perambulator_view.html'


class DilutionSchemeView(generic.DetailView):
    model = models.DilutionScheme
    template_name = 'lqcd_inventory/dilution_scheme_view.html'


class EnsembleView(generic.DetailView):
    model = models.Ensemble
    template_name = 'lqcd_inventory/ensemble_view.html'
