from django.urls import path
from galeria.views import imagem, index

urlpatterns = [
    path('', index, name='index'),
    path('imagem/', imagem, name='imagem')
]