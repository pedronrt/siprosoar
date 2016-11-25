from django.shortcuts import render
from django.views.generic import ListView
from licencias.models import Expediente

class IndexLicencias(ListView):
    template_name = 'licencias/index.html'
    model = Expediente
    context_object_name = 'lista_coordenadas'

