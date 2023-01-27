from django.urls import path
from .views import HoraExtraList

app_name = 'registro_hora_extra'

urlpatterns = [
    path('', HoraExtraList.as_view(), name='list'),
]
