from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blog import views

app_name = 'blog'


router = DefaultRouter()
router.register("posts", views.PostViewSet)

urlpatterns = [
    path("post.json", views.post_list),
    path("api/", include(router.urls)),
]