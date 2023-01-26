from django.shortcuts import render
from django.views.generic import CreateView

from .models import Documento


class DocumentoCreate(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']