from django.shortcuts import render

def index(request):
    return render(
        request,
        'core/index.html'
    )


def about(request):
    return render(
        request,
        'core/about.html'
    )


def life(request):
    return render(
        request,
        'core/life.html'
    )


def contacts(request):
    return render(
        request,
        'core/contacts.html'
    )