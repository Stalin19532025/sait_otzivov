from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('домашняя')
    template_name = 'users/регистрация.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
    
