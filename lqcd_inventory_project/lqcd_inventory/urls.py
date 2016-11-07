from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^dilution/(?P<pk>\d+)/view$', views.DilutionView.as_view(), name='dilution_view'),
    url(r'^eigensystem/(?P<pk>\d+)/view$', views.EigensystemView.as_view(), name='eigensystem_view'),
    url(r'^ensemble/(?P<pk>\d+)/view$', views.EnsembleView.as_view(), name='ensemble_view'),
    url(r'^perambulator/(?P<pk>\d+)/view$', views.PerambulatorView.as_view(), name='perambulator_view'),

    url(r'^dilution/$', views.DilutionList.as_view(), name='dilution_list'),
    url(r'^eigensystem/$', views.EigensystemList.as_view(), name='eigensystem_list'),
    url(r'^ensemble/$', views.EnsembleList.as_view(), name='ensemble_list'),
    url(r'^perambulator/$', views.PerambulatorList.as_view(), name='perambulator_list'),

    #url(r'^dilution/create$', views.dilution_schemes_create, name='dilution_schemes_create'),
    #url(r'^ensembles/create$', views.ensembles_create, name='ensembles_create'),
    url(r'^perambulator/create$', views.perambulators_create, name='perambulator_create'),

    url(r'^$', views.index, name='index'),
]
