from django.urls import reverse_lazy
from django.views import generic

from apps.accounts.forms import RegisterForm


class SignUpView(generic.CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy("login")
    template_name = "registration/sign_up.html"