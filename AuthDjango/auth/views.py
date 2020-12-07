from django.shortcuts import render
from auth import forms
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.
def auth_login(request):
    loginform=forms.LoginForm()
    error=None
    if request.method=='POST':
        loginform=forms.LoginForm(request.POST)
        if loginform.is_valid():
            username=loginform.cleaned_data['username']
            password=loginform.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user:
                login(request, user) # login() saves the user’s ID in the session, using Django’s session framework.
                # it is used to attach the user to the current session.
                return HttpResponseRedirect('/')
            else:
                error = "Invalid username or password"
    context={
    'loginform':loginform,
    'error':error,
    }
    return render(request,'auth/login.html',context=context)

# OR using generic login views

class Login(LoginView):
    template_name='auth/login.html'
    redirect_authenticated_user = True

class Logout(LogoutView):
    pass
