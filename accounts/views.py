from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import CreateView, TemplateView, View
from django.core.mail import EmailMessage
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model

from .forms import CustomUserCreationForm

User = get_user_model()


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        current_site = get_current_site(self.request)
        subject = "Confirme sua conta"
        message = render_to_string("registration/account_activation_email.html", {
            "user": user,
            "domain": current_site.domain,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": default_token_generator.make_token(user),
            "protocol": "https" if self.request.is_secure() else "http",
        })

        email = EmailMessage(subject, message, to=[user.email])
        email.send()

        messages.success(
            self.request,
            "Conta criada com sucesso. Verifique seu e-mail para ativar a conta."
        )
        return redirect("login")


class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, "Conta ativada com sucesso. Agora faça login.")
        else:
            messages.error(request, "Link de ativação inválido ou expirado.")

        return redirect("login")


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard.html"