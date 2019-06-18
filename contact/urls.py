from django.urls import path
from . import views

urlpatterns = [
    path('foundation/', views.index, name='index' ),
]