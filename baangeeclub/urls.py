from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

handler404 = 'home_baangee.views.handler404'
handler500 = 'home_baangee.views.handler500'
handler403 = 'home_baangee.views.handler403'
handler400 = 'home_baangee.views.handler400'

urlpatterns = [
    # Examples:
    url(r'^',include('home_baangee.urls')),
    url(r'^admin/', admin.site.urls),
]+ static(settings.MEDIA_ROOT, document_root=settings.MEDIA_URL)
