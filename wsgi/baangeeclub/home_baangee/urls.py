from django.conf.urls import include, url
from . import views


urlpatterns = [
	url(r'^$',views.index,name="index"),
	url(r'^soach/$',views.soach,name="soach"),
	url(r'^article/$',views.article_list,name="article_list"),
	url(r'^article/(?P<article_id>\d)/$',views.article,name="article"),
	url(r'^gallery/$',views.gallery,name="gallery"),
	url(r'^album/(?P<album_id>\d+)/$',views.album,name="album"),
]
