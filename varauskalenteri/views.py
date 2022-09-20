from http.client import HTTPResponse
from django.shortcuts import render

from .models import Tapahtuma


def tapahtumalistaus(request):
    tapahtumat = Tapahtuma.object.all()
    context ={
        'tapahtumat' : tapahtumat,
    }
    return render(request, 'listaus.html', context)


def varaa_tapahtuna(request, id):
    tapahtuma = Tapahtuma.objects.get{id=id}
    context = {'tapahtuma': tapahtuma}

    if request.method == "POST":
        varattu = tapahtuma.varaa(request.user)
        context
