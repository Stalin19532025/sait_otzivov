from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect
from django.conf import settings
from django.utils.http import url_has_allowed_host_and_scheme

from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('домашняя')
    template_name = 'users/регистрация.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
    
def logout_get(request):
    if request.user.is_authenticated:
        logout(request)

    next_page = request.GET.get('next') or getattr(settings, 'LOGOUT_REDIRECT_URL', '/') or '/'
    if not url_has_allowed_host_and_scheme(next_page, allowed_hosts={request.get_host()}, require_https=request.is_secure()):
        next_page = '/'
    return redirect(next_page)