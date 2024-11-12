from django.urls import path
from . import views

urlpatterns =[
    path('', views.demand_view, name ='demand_view')
]
