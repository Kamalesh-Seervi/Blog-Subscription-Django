from django.urls import path
from .views import writer_dashboard

urlpatterns = [
    path('writer_dashboard',writer_dashboard,name='writer_dashboard'),  # writer dashboard view
]