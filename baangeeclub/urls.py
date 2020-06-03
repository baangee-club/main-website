from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

handler404 = "home_baangee.views.handler404"
handler500 = "home_baangee.views.handler500"
handler403 = "home_baangee.views.handler403"
handler400 = "home_baangee.views.handler400"

urlpatterns = [
    # Examples:
    path("", include("home_baangee.urls")),
    path("epos/", include("epos.urls")),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_ROOT, document_root=settings.MEDIA_URL)
