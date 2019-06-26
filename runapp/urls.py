from django.urls import path
from . import views

app_name = 'runapp'

urlpatterns = [
    path('', views.index_run, name='index_run'),
]
