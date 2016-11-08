from django.forms import ModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.urls import reverse
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


class EigensystemForm(ModelForm):
    class Meta:
        model = models.Eigensystem
        fields = [
            'hyp_strength1',
            'hyp_strength2',
            'hyp_iterations',
            'eigenvector_count',
            'ev_ts_lambda_c',
            'ev_ts_lambda_l',
            'config_start',
            'config_end',
            'config_step',
            'path',
            'storage',
            'ensemble',
            'comment',
        ]


class DilutionForm(ModelForm):
    class Meta:
        model = models.DilutionScheme
        fields = ['name', 'letter', 'value']


class EnsembleForm(ModelForm):
    class Meta:
        model = models.Ensemble
        fields = ['name']


class PerambulatorForm(ModelForm):
    class Meta:
        model = models.Perambulator
        fields = [
            'ensemble',
            'storage',
            'mass_light',
            'mass_strange',
            'mass_charm',
            'dilution_source_time',
            'dilution_source_space',
            'dilution_source_laph',
            'dilution_source_dirac',
            'dilution_sink_time',
            'dilution_sink_space',
            'dilution_sink_laph',
            'dilution_sink_dirac',
            'comment',
        ]


def edit_generator(Model, Form, name):
    def edit(request, pk=None):
        obj_list = Model.objects.all()

        if request.method == 'POST':
            if pk is None:
                e = Model()
            else:
                e = Model.objects.get(pk=int(pk))
            form = Form(request.POST, instance=e)
            if form.is_valid():
                form.save() 
                return HttpResponseRedirect(reverse('{}_view'.format(name), args=[e.id]))
        else:
            if pk is None:
                form = Form()
            else:
                e = Model.objects.get(pk=int(pk))
                form = Form(instance=e)
        return render(request,
                      'lqcd_inventory/{}_edit.html'.format(name),
                      {'form': form})

    return edit


dilution_edit = edit_generator(models.DilutionScheme, DilutionForm, 'dilution')
eigensystem_edit = edit_generator(models.Eigensystem, EigensystemForm, 'eigensystem')
ensemble_edit = edit_generator(models.Ensemble, EnsembleForm, 'ensemble')
perambulator_edit = edit_generator(models.Perambulator, PerambulatorForm, 'perambulator')

def delete_generator(Model, name):
    def delete(request, pk):
        pass
    return delete

dilution_delete = delete_generator(models.DilutionScheme, 'dilution')
eigensystem_delete = delete_generator(models.Eigensystem, 'eigensystem')
ensemble_delete = delete_generator(models.Ensemble, 'ensemble')
perambulator_delete = delete_generator(models.Perambulator, 'perambulator')
