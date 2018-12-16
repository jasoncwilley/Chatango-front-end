from django.shortcuts import render, redirect
from  accounts.forms import RegistrationForm, AuthenticateForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout

from django.contrib.auth.forms import AuthenticationForm
def register(request):
    if request.method=='POST':
        reg_form = RegistrationForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            return HttpResponseRedirect('/')
    else:
        reg_form = RegistrationForm()

    args = {'reg_form':reg_form }
    return render(request, 'register.html', args)


def logout_view(request):
    logout(request)
    return redirect('/')



def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            # Success
            login(request, login_form.get_user())
            return redirect('/')
        else:
            # Failure
            login_form = AuthenticationForm()
            return render(request, 'user.html', {'login_form':login_form})
    
