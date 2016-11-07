from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^perambulator/create$', views.perambulators_create, name='perambulator_create'),
    url(r'^perambulator/(?P<pk>\d+)/view$', views.PerambulatorView.as_view(), name='perambulator_view'),
    url(r'^perambulator/$', views.PerambulatorList.as_view(), name='perambulator_index'),
    #url(r'^dilution_schemes/create$', views.dilution_schemes_create, name='dilution_schemes_create'),
    url(r'^dilution_scheme/(?P<pk>\d+)/view$', views.DilutionSchemeView.as_view(), name='dilution_scheme_view'),
    #url(r'^dilution_schemes/$', views.dilution_schemes_index, name='dilution_schemes_index'),
    #url(r'^ensembles/create$', views.ensembles_create, name='ensembles_create'),
    url(r'^ensemble/(?P<pk>\d+)/view$', views.EnsembleView.as_view(), name='ensemble_view'),
    #url(r'^ensembles/$', views.ensembles_index, name='ensembles_index'),
    url(r'^$', views.index, name='index'),
]
