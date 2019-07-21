from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect, reverse


class HomeView(TemplateView):
    template_name = 'home.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_anonymous:
            return redirect(reverse('google_photos:dashboard'))
        return super(HomeView, self).dispatch(request, *args, **kwargs)


class DashboardView(TemplateView):
    template_name = 'dashboard.html'
