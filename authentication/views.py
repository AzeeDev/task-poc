from django.shortcuts import render
from django.views import View
from authentication.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect


# Create your views here.
class RegisterView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'signup.html', context={'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = RegistrationForm(request.POST)
        return render(request, 'signup.html', context={'form': form})


class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', context={'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            form = AuthenticationForm()

        return render(request, 'registration.html', context={'form': form})
