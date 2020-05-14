from django.shortcuts import render
from django.views import View

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

            print(form.cleaned_data)

        context = {
            'form': form,
        }

        return render(request, 'users/login.html', context=context)
