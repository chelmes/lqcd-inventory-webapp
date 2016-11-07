from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from . import models


def index(request):
    return render(request, 'lqcd_inventory/index.html')


def perambulators_create(request):
    return render(request, 'lqcd_inventory/404.html')


class PerambulatorList(generic.ListView):
    model = models.Perambulator
    template_name = 'lqcd_inventory/perambulator_list.html'


class PerambulatorView(generic.DetailView):
    model = models.Perambulator
    template_name = 'lqcd_inventory/perambulator_view.html'


class DilutionList(generic.ListView):
    model = models.DilutionScheme
    template_name = 'lqcd_inventory/dilution_list.html'


class DilutionView(generic.DetailView):
    model = models.DilutionScheme
    template_name = 'lqcd_inventory/dilution_view.html'


class EnsembleList(generic.ListView):
    model = models.Ensemble
    template_name = 'lqcd_inventory/ensemble_list.html'


class EnsembleView(generic.DetailView):
    model = models.Ensemble
    template_name = 'lqcd_inventory/ensemble_view.html'


class EigensystemList(generic.ListView):
    model = models.Eigensystem
    template_name = 'lqcd_inventory/eigensystem_list.html'


class EigensystemView(generic.DetailView):
    model = models.Eigensystem
    template_name = 'lqcd_inventory/eigensystem_view.html'
