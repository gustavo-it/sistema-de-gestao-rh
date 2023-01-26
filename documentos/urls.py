from django.urls import path

from .views import DocumentoCreate

app_name = 'documentos'

urlpatterns = [
    path('novo/', DocumentoCreate.as_view(), name='create'),
]
