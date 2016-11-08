from django.forms import ModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.urls import reverse
from django.views import generic

from . import models

def index(request):
    return render(request, 'lqcd_inventory/index.html')

###############################################################################

class DilutionForm(ModelForm):
    class Meta:
        model = models.Dilution
        fields = ['name', 'letter', 'value']

class DilutionList(generic.ListView):
    model = models.Dilution
    template_name = 'lqcd_inventory/dilution_list.html'

class DilutionView(generic.DetailView):
    model = models.Dilution
    template_name = 'lqcd_inventory/dilution_view.html'

###############################################################################

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

class EigensystemList(generic.ListView):
    model = models.Eigensystem
    template_name = 'lqcd_inventory/eigensystem_list.html'

class EigensystemView(generic.DetailView):
    model = models.Eigensystem
    template_name = 'lqcd_inventory/eigensystem_view.html'

###############################################################################

class EnsembleForm(ModelForm):
    class Meta:
        model = models.Ensemble
        fields = ['name']

class EnsembleList(generic.ListView):
    model = models.Ensemble
    template_name = 'lqcd_inventory/ensemble_list.html'

class EnsembleView(generic.DetailView):
    model = models.Ensemble
    template_name = 'lqcd_inventory/ensemble_view.html'

###############################################################################

def perambulators_create(request):
    return render(request, 'lqcd_inventory/404.html')

class PerambulatorForm(ModelForm):
    class Meta:
        model = models.Perambulator
        fields = [
            'quark_type',
            'mass',
            'eigensystem',
            'storage',
            'config_start',
            'config_end',
            'config_step',
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

class PerambulatorList(generic.ListView):
    model = models.Perambulator
    template_name = 'lqcd_inventory/perambulator_list.html'

class PerambulatorView(generic.DetailView):
    model = models.Perambulator
    template_name = 'lqcd_inventory/perambulator_view.html'

###############################################################################

class PerambulatorSeedForm(ModelForm):
    class Meta:
        model = models.PerambulatorSeed
        fields = ['seed_id', 'seed', 'perambulator']

class PerambulatorSeedList(generic.ListView):
    model = models.PerambulatorSeed
    template_name = 'lqcd_inventory/perambulator_seed_list.html'

class PerambulatorSeedView(generic.DetailView):
    model = models.PerambulatorSeed
    template_name = 'lqcd_inventory/perambulator_seed_view.html'

###############################################################################

class StorageForm(ModelForm):
    class Meta:
        model = models.Storage
        fields = ['name', 'account', 'path']

class StorageList(generic.ListView):
    model = models.Storage
    template_name = 'lqcd_inventory/storage_list.html'

class StorageView(generic.DetailView):
    model = models.Storage
    template_name = 'lqcd_inventory/storage_view.html'

###############################################################################

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

dilution_edit = edit_generator(models.Dilution, DilutionForm, 'dilution')
eigensystem_edit = edit_generator(models.Eigensystem, EigensystemForm, 'eigensystem')
ensemble_edit = edit_generator(models.Ensemble, EnsembleForm, 'ensemble')
perambulator_edit = edit_generator(models.Perambulator, PerambulatorForm, 'perambulator')
perambulator_seed_edit = edit_generator(models.PerambulatorSeed, PerambulatorSeedForm, 'perambulator_seed')
storage_edit = edit_generator(models.Storage, StorageForm, 'storage')

def delete_generator(Model, name):
    def delete(request, pk):
        pass
    return delete

dilution_delete = delete_generator(models.Dilution, 'dilution')
eigensystem_delete = delete_generator(models.Eigensystem, 'eigensystem')
ensemble_delete = delete_generator(models.Ensemble, 'ensemble')
perambulator_delete = delete_generator(models.Perambulator, 'perambulator')
perambulator_seed_delete = delete_generator(models.PerambulatorSeed, 'perambulator_seed')
storage_delete = delete_generator(models.Storage, 'storage')
