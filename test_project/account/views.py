from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

def login(request):
  return render(request, 'login.html')

def signup(request):
  return render(request, 'signup.html')

def main(request):
  return render(request, 'main.html')

def index(request):
  return redirect('login')