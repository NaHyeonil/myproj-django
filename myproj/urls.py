from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include("blog.urls")),
    path('news/', include("news.urls")),
    path('shop/', include("shop.urls")),
]