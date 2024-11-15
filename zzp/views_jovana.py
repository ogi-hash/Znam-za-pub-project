from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import *
from .views_civotamarev import recenzija_req
from datetime import datetime
from django.db.models import F, Min

def kvizovi_req(request: HttpRequest):
    """
        Funkcija koja obradjuje zahtev za prikazom stranice kvizova

        Args:
            request (HttpRequest): zahtev za generisanje stranice

        Returns:
            HttpResponse: generise stranicu kvizova
    """

    kvizovi = Kviz.objects.all()

    contex = {
        "kvizovi": kvizovi,
        "poruka": ""
    }

    return render(request, "kvizovi.html", contex)

def organizatori_req(request: HttpRequest):
    """
        Funkcija koja obradjuje zahtev za prikazom stranice organizatora

        Args:
            request (HttpRequest): zahtev za generisanje stranice

        Returns:
            HttpResponse: generise stranicu organizatora
    """

    organizatori = Organizator.objects.all()
    # kvizovi = Kviz.objects.filter(datumvreme__gt=datetime.now()).order_by('datumvreme')
    #
    # organizacije = Organizator.objects.values('idorg', 'naziv').annotate(
    #     najskoriji_kviz=Min('kviz__datumvreme')).order_by('najskoriji_kviz')
    #
    # for organizacija in organizacije:
    #     najskoriji_kviz = Kviz.objects.filter(idorg=organizacija['idorg'],
    #                                            datumvreme=organizacija['najskoriji_kviz']).first()

    contex = {
        "organizatori": organizatori,
        # "kvizovi": kvizovi,
    }

    return render(request, "organizacije.html", contex)

def org_req(request: HttpRequest, org_id):
    """
        Funkcija koja obradjuje zahtev za prikazom stranice kvizova

        Args:
            request (HttpRequest): zahtev za generisanje stranice, id organizacije ciju stranicu generisemo

        Returns:
            HttpResponse: generise stranicu odgovarajuceg organizatora
    """

    organizator = Organizator.objects.get(idorg=org_id)


    context = {
        # "organizator": organizator
    }

    context = recenzija_req(request, org_id, context)

    if (context["ocene"] != []):
        prosek = sum(context["ocene"]) / len(context["ocene"])
        prosek = int(round(prosek))
    else:
        prosek = 0

    context["organizator"] = organizator
    context["prosek"] = prosek

    return render(request, 'org_strana.html', context)

