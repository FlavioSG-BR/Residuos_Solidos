from django.shortcuts import render
from core.models import Evento

# Create your views here.


def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.all()
    dados = {'evento':evento}
    return render(request, 'Informacoes.html', dados)
