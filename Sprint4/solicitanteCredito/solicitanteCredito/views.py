from urllib import request
from .models import Solicitante
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
import json

def check_pago(data):
    r = request.get(settings.PATH_VAR, headers={"Accept":"application/json"})
    pagos = r.json()
    for pago in pagos:
        if data["pago"] == pago["id"]:
            return True
    return False

def SolicitanteList(request):
    queryset = Solicitante.objects.all()
    context = list(queryset.values('id', 'pago', 'empresa'))
    return JsonResponse(context, safe=False)

def SolicitanteCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        if check_pago(data_json) == True:
            solicitante = Solicitante()
            solicitante.pago = data_json['pago']
            solicitante.empresa = data_json['empresa']
            solicitante.save()
            return HttpResponse("successfully created solicitante")
        else:
            return HttpResponse("unsuccessfully created solicitante. Pago does not exist")

            
def SolicitanteCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        solicitante_list = []
        for solicitante in data_json:
                    if check_pago(solicitante) == True:
                        db_solicitante = Solicitante()
                        db_solicitante.pago = solicitante['pago']
                        db_solicitante.empresa = solicitante['empresa']
                        solicitante_list.append(db_solicitante)
                    else:
                        return HttpResponse("unsuccessfully created solicitante. Pago does not exist")
        
        Solicitante.objects.bulk_create(solicitante_list)
        return HttpResponse("successfully created solicitante")