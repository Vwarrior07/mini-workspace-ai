from django.urls import path
from .views import health_status

urlpatterns = [
    path("", health_status, name="health_status"),
]
