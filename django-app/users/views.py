from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.views.generic import FormView

from users.forms import LoginForm, SignUpForm

User = get_user_model()


class LoginView(FormView):

    template_name = "users/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


class LogoutView(View):

    def get(self, request):

        logout(request)

        return redirect("core:home")


class SignUpView(FormView):
    template_name = "users/signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("core:home")

    initial = {
        'first_name': 'Kim',
        'last_name': 'YongYeon',
        'email': 'test@gmail.com',
    }

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        user.verify_email()
        return super().form_valid(form)


def complete_verification(request, key):

    try:
        user = User.objects.get(email_secret=key)
        user.email_verified = True
        user.email_secret = ""
        user.save()
        # to do : add success messabe
    except User.DoesNotExist:
        # to do : add error message
        pass
    return redirect("core:home")
