from django.shortcuts import render, HttpResponse
from .utils import generation_key
from django.core.cache import cache
from .models import Metric

def index(request):
    generation = generation_key()
    key = 'dashboard:index'

    data = cache.get(key, version=generation)
    if data is None:
        metrics = []
        for MC in Metric.__subclasses__():
            metrics.extend(MC.objects.filter(show_on_dashboard=True))
        
        data = []
        cache.set(key, data, 60 * 60, version=generation)

    return render(request, 'dashboard/index.html', {'data': data})
