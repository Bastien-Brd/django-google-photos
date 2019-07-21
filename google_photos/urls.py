from django.urls import path, include

from .views import HomeView, DashboardView


app_name = "google_photos"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard', DashboardView.as_view(), name='dashboard'),
]
