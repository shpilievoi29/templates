from random import randint

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def product(request):
    return HttpResponse(product)


def contacts(request):
    return HttpResponse('page of contacts')


def contact_list(request):
    context = {
        'title': 'Contact list',
        'Contacts': [
            {"title": "Contact #1", "url": "contact-1"},
            {"title": "Contact #2", "url": "contact-2"},
            {"title": "Contact #3", "url": "contact-3"},
            {"title": "Contact #4", "url": "contact-4"},
            {"title": "Contact #5", "url": "contact-5"},
            {"title": "Contact #6", "url": "contact-6"},
            {"title": "Contact #7", "url": "contact-7"},
            {"title": "Contact #8", "url": "contact-8"},
            {"title": "Contact #9", "url": "contact-9"},
        ], }

    return render(request, "contact.html", context)


def contact_detail(request, contact_slug):
    return render(request, "contact_detail.html", {"contact_slug": contact_slug})
