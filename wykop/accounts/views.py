from django.shortcuts import redirect
from django.views.generic import CreateView

from wykop.accounts.forms import RegistrationForm


class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'accounts/registration.html'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)
