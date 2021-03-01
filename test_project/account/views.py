from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import auth

def login(request):
  if request.method == 'POST':
    email = request.POST['email']
    password = request.POST['password']
    user = auth.authenticate(request, email=email, password=password)
    if user is not None:
      auth.login(request, user)
      return redirect('main')
    else:
      return render(request, 'login.html', {'error' : 'email or password not correct'})

  return render(request, 'login.html')

def signup(request):
  if request.method == 'POST':
    if request.POST['password1'] == request.POST['password2']:
      email = request.POST['email']
      username = request.POST['username']
      role = request.POST['role']
      password = request.POST['password1']
      user = get_user_model().objects.create_user(
        email=email, username=username, role=role, password=password
        )
      auth.login(request, user)
      return redirect('main')
    else:
      return render(request, 'signup.html', {'error' : 'password not matched'})
  return render(request, 'signup.html')

def main(request):
  return render(request, 'main.html')

def index(request):
  return redirect('login')

def logout(request):
  auth.logout(request)
  return redirect('login')