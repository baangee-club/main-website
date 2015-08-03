from django.conf.urls import patterns, include, url
from django.conf.urls import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

handler404 = 'home_baangee.views.handler404'
handler500 = 'home_baangee.views.handler500'

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^',include('home_baangee.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_ROOT, document_root=settings.MEDIA_URL)
