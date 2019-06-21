from django.shortcuts import render, HttpResponse
from .utils import generation_key
from django.core.cache import cache
from .models import Metric

def index(request):
    generation = generation_key()
    key = 'dashboard:index'

    data = cache.get(key, version=generation)
    subClassModel = Metric.__subclasses__()
    # for x in subClassModel:
    #     print(x.toitinma('mimi'))

    # if data is None:
    #     metrics = []
    #     subClassModel = Metric.__subclasses__()
    #     for x in subClassModel:
    #         print(x.toitinma('mimi'))
        
    #     data = []
    #     cache.set(key, data, 60 * 60, version=generation)

    return render(request, 'dashboard/index.html', {'data': data})
