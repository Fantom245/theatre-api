from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    #Api
    path("api/", include("play.urls")),
    path("api/", include("performance.urls")),
    path("api/", include("theatrehall.urls")),
    path("api/", include("ticket.urls")),
    path("api/", include("users.urls")),

    #HTML
    path("", include("play.html_urls")),
    path("", include("theatrehall.html_urls"))
]
