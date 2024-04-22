from django.shortcuts import render

from django.contrib.auth import login
from django.shortcuts import render, redirect
from .models import User, UseInviteCode
from .forms import PhoneLoginForm, AcceptCode, Profile
import random
import string
import time


def generate_code():
    chars = string.ascii_letters + string.digits
    code = ''.join(random.choice(chars) for _ in range(6))
    return code


def phone_login(request):
    if request.method == 'POST':
        form = PhoneLoginForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            time.sleep(2)
            request.session['phone_number'] = phone_number
            return redirect('phone_login_code')
    else:
        form = PhoneLoginForm()

    return render(request, 'login.html', {'form': form})


def phone_login_code(request):
    if request.method == 'POST':
        form = AcceptCode(request.POST)
        if form.is_valid():
            phone = request.session['phone_number']
            if User.objects.filter(phone=phone).exists():
                return redirect('profile')
            else:
                user = User.objects.create(phone=phone, invite_code=generate_code())
                return redirect('profile')
    else:
        form = AcceptCode()

    return render(request, 'login_accept_code.html', {'form': form})


def profile(request):
    if request.method == 'POST':
        form = Profile(request.POST)
        if form.is_valid():
            if User.objects.filter(invite_code=form.cleaned_data['activate']).exists():
                obj = User.objects.get(invite_code=form.cleaned_data['activate'])
                UseInviteCode.objects.create(user_id=obj, who_used_code=request.session['phone_number'])
                obj.active = True
                obj.save()
    else:
        form = Profile()
    try:
        phone = request.session['phone_number']
        obj = User.objects.get(phone=phone)
        invite_code = obj.invite_code
        active = obj.active
        invite_numbers = UseInviteCode.objects.filter(user_id=obj.id)
    except User.DoesNotExist:
        return redirect('login')

    context = {'phone': phone, 'invite_code': invite_code, 'active': active, 'invite_numbers': invite_numbers,
               'form': form}
    return render(request, 'profile.html', context)
