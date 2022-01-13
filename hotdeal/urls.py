from django.urls import path, include
from rest_framework.routers import DefaultRouter

from hotdeal import views


app_name = 'hotdeal'


router = DefaultRouter()
router.register("hotdeals", views.HotdealViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]