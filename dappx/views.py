# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

# dappx/views.py

from django.shortcuts import render
from dappx.forms import UserForm,TutorQuestionForm,AcademicStudentInfoForm,YogaStudentInfoForm,MusicStudentInfoForm,DanceStudentInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'dappx/index.html')

#def signup(request):
 #   return render(request,'dappx/register1.html')

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = AcademicStudentInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = AcademicStudentInfoForm()
    return render(request,'dappx/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})


def TutorRegister(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form1 = TutorQuestionForm(data=request.POST)
        if user_form.is_valid() and profile_form1.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form1.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form1.errors)
    else:
        user_form = UserForm()
        profile_form1 = TutorQuestionForm()
    return render(request,'dappx/registration1.html',
                          {'user_form':user_form,
                           'profile_form1':profile_form1,
                           'registered':registered})


def danceRegister(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form3= DanceStudentInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form3.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form3.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form3 = DanceStudentInfoForm()
    return render(request,'dappx/DanceRegister.html',
                          {'user_form':user_form,
                           'profile_form3':profile_form3,
                           'registered':registered})

def yogaRegister(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form4= YogaStudentInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form4.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form4.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form4 = YogaStudentInfoForm()
    return render(request,'dappx/YogaRegister.html',
                          {'user_form':user_form,
                           'profile_form4':profile_form4,
                           'registered':registered})
def musicRegister(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form5= MusicStudentInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form5.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form5.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form5.errors)
    else:
        user_form = UserForm()
        profile_form5 = MusicStudentInfoForm()
    return render(request,'dappx/MusicRegister.html',
                          {'user_form':user_form,
                           'profile_form5':profile_form5,
                           'registered':registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'dappx/login.html', {})
