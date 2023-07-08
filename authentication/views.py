from django.shortcuts import render
from django.views import View
from authentication.forms import (RegistrationForm,
                                  CustomAuthenticationForm
                                )
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
class RegisterView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'signup.html', context={'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request=request, message='User registered successfully !')
        else:
            form = RegistrationForm(request.POST)
        return render(request, 'signup.html', context={'form': form})


class UserLoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        form = CustomAuthenticationForm()
        return render(request, 'login.html', context={'form': form})

    def post(self, request):
        form = CustomAuthenticationForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request=request, message='Invalid credentials ! ')

        return render(request, 'login.html', context={'form': form})

class UserLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'User logout successfully ! ')
        return redirect('login')