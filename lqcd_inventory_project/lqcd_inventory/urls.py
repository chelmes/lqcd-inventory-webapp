from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^perambulators/create$', views.perambulators_create, name='perambulators_create'),
    url(r'^perambulators/(?P<pk>\d+)/view$', views.PerambulatorView.as_view(), name='perambulators_view'),
    url(r'^perambulators/$', views.perambulators_index, name='perambulators_index'),
    #url(r'^dilution_schemes/create$', views.dilution_schemes_create, name='dilution_schemes_create'),
    url(r'^dilution_schemes/(?P<pk>\d+)/view$', views.DilutionSchemeView.as_view(), name='dilution_schemes_view'),
    #url(r'^dilution_schemes/$', views.dilution_schemes_index, name='dilution_schemes_index'),
    #url(r'^ensembles/create$', views.ensembles_create, name='ensembles_create'),
    url(r'^ensembles/(?P<pk>\d+)/view$', views.EnsembleView.as_view(), name='ensembles_view'),
    #url(r'^ensembles/$', views.ensembles_index, name='ensembles_index'),
    url(r'^$', views.index, name='index'),
]
