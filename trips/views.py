from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'trips/index.html')
