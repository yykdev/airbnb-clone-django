import os

import requests
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.views.generic import FormView

from users.forms import LoginForm, SignUpForm
from utils import Constant

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


def github_login(request):
    client_id = os.environ.get("GITHUB_CLIENT_ID")
    redirect_uri = os.environ.get("GITHUB_REDIRECT_URI")
    return redirect("https://github.com/login/oauth/authorize?client_id={}&redirect_uri={}&scope=read:user".format(client_id, redirect_uri))


class GithubException(Exception):

    pass


def github_callback(request):
    try:
        client_id = os.environ.get("GITHUB_CLIENT_ID")
        secret_id = os.environ.get("GITHUB_CLIENT_SECRET")
        code = request.GET.get("code", None)
        if code is not None:
            token_requests = requests.post(
                "https://github.com/login/oauth/access_token?client_id={}&client_secret={}&code={}".format(client_id, secret_id, code),
                headers={"Accept": "application/json"}
            )
            token_json = token_requests.json()
            error = result_json.get("error", None)
            if error is not None:
                raise GithubException()
            else:
                access_token = token_json.get("access_token")
                profile_request = requests.get(
                    "https://api.github.com/user",
                    headers={
                        "Authorization": "token {}".format(access_token)
                    }
                )
                profile_json = profile_request.json()
                username = profile_json.get("login", None)
                if username is not None:
                    name = profile_json.get("name")
                    email = profile_json.get("email")
                    bio = profile_json.get("bio")

                    try:
                        user = User.objects.get(email=email)
                        if user.login_method != Constant.LOGIN_GITHUB:
                            raise GithubException()
                    except User.DoesNotExist:
                        user = User.objects.create(
                            email=email,
                            first_name=name,
                            username=email,
                            bio=bio if bio else "",
                            login_method=Constant.LOGIN_GITHUB,
                        )
                        user.set_unusable_password()
                        user.save()
                    login(request, user)
                    return redirect("core:home")
                else:
                    raise GithubException()
        raise GithubException()
    except Exception as e:
        print(e)
        # send error message
        return redirect("users:login")
