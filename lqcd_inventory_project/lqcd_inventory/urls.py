from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^dilution/(?P<pk>\d+)/view$', views.DilutionView.as_view(), name='dilution_view'),
    url(r'^eigensystem/(?P<pk>\d+)/view$', views.EigensystemView.as_view(), name='eigensystem_view'),
    url(r'^ensemble/(?P<pk>\d+)/view$', views.EnsembleView.as_view(), name='ensemble_view'),
    url(r'^perambulator/(?P<pk>\d+)/view$', views.PerambulatorView.as_view(), name='perambulator_view'),
    url(r'^perambulator_seed/(?P<pk>\d+)/view$', views.PerambulatorSeedView.as_view(), name='perambulator_seed_view'),
    url(r'^storage/(?P<pk>\d+)/view$', views.StorageView.as_view(), name='storage_view'),

    url(r'^dilution/(?P<pk>\d+)/edit$', views.dilution_edit, name='dilution_edit'),
    url(r'^eigensystem/(?P<pk>\d+)/edit$', views.eigensystem_edit, name='eigensystem_edit'),
    url(r'^ensemble/(?P<pk>\d+)/edit$', views.ensemble_edit, name='ensemble_edit'),
    url(r'^perambulator/(?P<pk>\d+)/edit$', views.perambulator_edit, name='perambulator_edit'),
    url(r'^perambulator_seed/(?P<pk>\d+)/edit$', views.perambulator_seed_edit, name='perambulator_seed_edit'),
    url(r'^storage/(?P<pk>\d+)/edit$', views.storage_edit, name='storage_edit'),

    url(r'^dilution/(?P<pk>\d+)/delete$', views.dilution_delete, name='dilution_delete'),
    url(r'^eigensystem/(?P<pk>\d+)/delete$', views.eigensystem_delete, name='eigensystem_delete'),
    url(r'^ensemble/(?P<pk>\d+)/delete$', views.ensemble_delete, name='ensemble_delete'),
    url(r'^perambulator/(?P<pk>\d+)/delete$', views.perambulator_delete, name='perambulator_delete'),
    url(r'^perambulator_seed/(?P<pk>\d+)/delete$', views.perambulator_seed_delete, name='perambulator_seed_delete'),
    url(r'^storage/(?P<pk>\d+)/delete$', views.storage_delete, name='storage_delete'),

    url(r'^dilution/create$', views.dilution_edit, name='dilution_create'),
    url(r'^eigensystem/create$', views.eigensystem_edit, name='eigensystem_create'),
    url(r'^ensemble/create$', views.ensemble_edit, name='ensemble_create'),
    url(r'^perambulator/create$', views.perambulator_edit, name='perambulator_create'),
    url(r'^perambulator_seed/create$', views.perambulator_seed_edit, name='perambulator_seed_create'),
    url(r'^storage/create$', views.storage_edit, name='storage_create'),

    url(r'^dilution/$', views.DilutionList.as_view(), name='dilution_list'),
    url(r'^eigensystem/$', views.EigensystemList.as_view(), name='eigensystem_list'),
    url(r'^ensemble/$', views.EnsembleList.as_view(), name='ensemble_list'),
    url(r'^perambulator/$', views.PerambulatorList.as_view(), name='perambulator_list'),
    url(r'^perambulator_seed/$', views.PerambulatorSeedList.as_view(), name='perambulator_seed_list'),
    url(r'^storage/$', views.StorageList.as_view(), name='storage_list'),

    url(r'^$', views.index, name='index'),
]
