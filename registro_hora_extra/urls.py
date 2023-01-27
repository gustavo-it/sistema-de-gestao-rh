from django.urls import path
from .views import HoraExtraList, HoraExtraEdit, HoraExtraDelete

app_name = 'registro_hora_extra'

urlpatterns = [
    path('', HoraExtraList.as_view(), name='list'),
    path('editar/<int:pk>/', HoraExtraEdit.as_view(), name='update'),
    path('delete/<int:pk>/', HoraExtraDelete.as_view(), name='delete')
]
