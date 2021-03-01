from django.shortcuts import render, redirect

def login(request):
  return render(request, 'login.html')

def signup(request):
  return render(request, 'signup.html')

def main(request):
  return render(request, 'main.html')

def index(request):
  return redirect('login')