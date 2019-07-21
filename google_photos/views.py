import requests

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

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)

        social = self.request.user.social_auth.get(provider='google-oauth2')
        try:
            response = requests.get(
                'https://photoslibrary.googleapis.com/v1/mediaItems?pageSize=25',
                params={'access_token': social.extra_data['access_token']},
                timeout=10,
            )
            response_json = response.json()
            media_items = response_json.get('mediaItems', [])

            context['last_photo'] = media_items[0]
        except requests.exceptions.Timeout:
            context['last_photo'] = None
            context['error'] = 'The request to the Google API timed out.'

        return context