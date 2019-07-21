from django.urls import path, include
from django.views.generic import TemplateView

app_name = "google_photos"

urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html")),
]
