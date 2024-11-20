from django.urls import path
from demand import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", views.demand_view, name="demand_view"),
    # path('<int:print_id>/', views.demand_detail , name ='demand_detail'),
    path("demand_add/", views.demand_add, name="demand_add"),
    path("demand_detail/<int:post_id>/", views.demand_detail, name="demand_detail"),
    path("api/demand_list/", views.api_tbDemand.as_view(), name="api_tbDemand"),
    path("api/demand_list/<int:post_id>/", views.api_tbDemand_detail.as_view(), name="api_tbDemand_detail"),
    path("api/demand_list/<int:post_id>/put_title/", views.api_tbDemand_detail_put_title.as_view(), name="api_tbDemand_detail_put_title"),
    path("api/demand_list/<int:post_id>/put_image/", views.api_tbDemand_detail_put_image.as_view(), name="api_tbDemand_detail_put_image"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
