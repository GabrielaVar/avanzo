from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^solicitanteCredito/', views.SolicitanteList),
    url(r'^solicitantecreate/$', csrf_exempt(views.SolicitanteCreate), name='solicitanteCreate'),
    url(r'^createsolicitante/$', csrf_exempt(views.SolicitanteCreate), name='createSolicitante'),
]