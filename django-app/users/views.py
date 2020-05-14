from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from users.forms import LoginForm


class LoginView(View):

    def get(self, request):

        form = LoginForm()

        context = {
            'form': form,
        }

        return render(request, 'users/login.html', context=context)

    def post(self, request):

        form = LoginForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)

                return redirect("core:home")

        context = {
            'form': form,
        }

        return render(request, 'users/login.html', context=context)
