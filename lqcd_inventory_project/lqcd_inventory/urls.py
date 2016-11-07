from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^parambulators/create$', views.parambulators_create, name='parambulators_create'),
    url(r'^parambulators/(?:P<parambulator_id>\d+)/view$', views.parambulators_view, name='parambulators_view'),
    url(r'^parambulators/$', views.parambulators_index, name='parambulators_index'),
    url(r'^$', views.index, name='index'),
]
