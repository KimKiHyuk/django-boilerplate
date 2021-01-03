from django.urls import path
from .views import visit, ack
urlpatterns = [
    path('visit/', visit),
    path('ack/', ack)
]
