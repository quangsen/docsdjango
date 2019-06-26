from django.shortcuts import render
from django.shortcuts import HttpResponse


def index_run(request):
    return HttpResponse("hello run")
