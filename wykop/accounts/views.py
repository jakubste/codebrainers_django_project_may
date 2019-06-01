from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, View

from wykop.accounts.forms import RegistrationForm
from wykop.accounts.models import User


class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'accounts/registration.html'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)


class BanUserView(View):
    def post(self, request, *args, **kwargs):
        user_pk = kwargs.get('user_pk')
        user = User.objects.get(pk=user_pk)
        user.banned = request.POST.get('set') == '1'
        user.save()

        return redirect(
            request.META.get('HTTP_REFERER', reverse('posts:list'))
        )
