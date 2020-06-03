from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path(
        "<str:scheme>/<str:type>/<int:month>/<int:year>/", views.report, name="report",
    ),
]
