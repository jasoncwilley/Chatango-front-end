from django.shortcuts import render, redirect
from  accounts.forms import RegistrationForm, AuthenticationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

def register(request):
    if request.method=='POST':
        reg_form = RegistrationForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            return HttpResponseRedirect('chats/latestspam.html')
    else:
        reg_form = RegistrationForm()

    args = {'reg_form':reg_form }
    return render(request, 'register.html', args)

def logout_view(request):
    
    return redirect('/')

def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        if form.is_valid():
                        # Success
            user = login_form.get()
            login(request, user)
            return HttpResponseRedirect('chats/latestspam.html')
    else:
            # Failure
        login_form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'login_form':login_form})
