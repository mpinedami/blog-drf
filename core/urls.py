from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("apps.posts.urls")),
    path(r"auth/", include("djoser.urls")),
    # path(r"auth/", include("djoser.urls.authtoken")),
    path(r"auth/", include("djoser.urls.jwt")),
]
