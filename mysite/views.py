from django.shortcuts import render, redirect
from .form import SignUpForm
from django.contrib.auth import login, authenticate

import logging
logger = logging.getLogger(__name__)

def error_404(request, exception):
  return render(request,'errors/404.html')

def error_500(request):
  return render(request,'errors/500.html')

def error_400(request, exception):
  return render(request,'errors/400.html')

def error_403(request, exception):
  return render(request,'errors/403.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/sign_up.html', {'form': form})