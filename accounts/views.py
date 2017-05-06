from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth.decorators import login_required
# from app.forms import *

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, '회원가입 했습니다.')
            return redirect(settings.LOGIN_URL)


    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html',{
        'form':form,
    })

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')
