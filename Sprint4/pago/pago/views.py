from .models import Pago
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
import json

def PagoList(request):
    queryset = Pago.objects.all()
    context = list(queryset.values('id', 'valor', 'descuento', 'descripcion'))
    return JsonResponse(context, safe=False)

def PagoCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        pago = Pago()
        pago.valor = data_json["valor"]
        pago.descuento = data_json["descuento"]
        pago.descripcion = data_json["descripcion"]
        pago.save()
        return HttpResponse("successfully created pago")