from django.urls import path
from .views import client_dashboard

urlpatterns = [
    path('client-dashboard', client_dashboard, name='client_dashboard'),  # i am adding url path client dashboard view
]