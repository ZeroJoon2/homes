from django.urls import path, include
from . import views

urlpatterns =[
    path('login/', views.register_user, name = 'login'),
    path('', views.login_check, name = 'login_check'),
    path('demand/', include('demand.urls')),
    #path('select/demand', demand_view, name = 'demand_view'),
    #path('login/', views.login, name = 'login'),
]
