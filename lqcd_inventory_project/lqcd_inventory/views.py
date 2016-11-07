from django.shortcuts import render
from django.http import HttpResponse

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


def perambulators_view(request, perambulator_id):
    return render(request, 'lqcd_inventory/404.html')
