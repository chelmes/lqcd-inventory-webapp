from django.shortcuts import render
from django.http import HttpResponse

from . import models


def index(request):
    return render(request, 'lqcd_inventory/index.html')


def parambulators_index(request):
    parambulator_list = models.Perambulator.objects

    return render(
        request,
        'lqcd_inventory/parambulators_index.html',
        perambulator_list=perambulator_list,
    )


def parambulators_create(request):
    return render(request, 'lqcd_inventory/404.html')


def parambulators_view(request, parambulator_id):
    return render(request, 'lqcd_inventory/404.html')
