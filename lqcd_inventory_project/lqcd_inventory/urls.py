from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^perambulators/create$', views.perambulators_create, name='perambulators_create'),
    url(r'^perambulators/(?:P<perambulator_id>\d+)/view$', views.perambulators_view, name='perambulators_view'),
    url(r'^perambulators/$', views.perambulators_index, name='perambulators_index'),
    url(r'^$', views.index, name='index'),
]
