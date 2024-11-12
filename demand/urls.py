from django.urls import path
from demand import views
urlpatterns =[
    path('', views.demand_view, name ='demand_view'),
    #path('<int:print_id>/', views.demand_detail , name ='demand_detail'),
    path('demand_add/', views.demand_add , name ='demand_add'),
]
