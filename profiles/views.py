from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User, Group
from profiles.models import UserProfile, GroupProfile

from profiles import forms


def view_user(request, user_name):
    try:
        user = User.objects.get(username=user_name)
    except User.DoesNotExist:
        raise Http404()

    context = {
        'user': user,
    }
    return render(request, 'profiles/view_profile.html', context)


def view_group(request, group_id):
    try:
        group = Group.objects.get(pk=group_id)
        group_profile = group.groupprofile
    except Group.DoesNotExist:
        raise Http404()

    context = {
        'group': group,
        'group_profile': group_profile
    }
    return render(request, 'profiles/view_group.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        user = authenticate(username=username, password=password)

        if user and user.is_active:
            login(request, user)
            return HttpResponseRedirect('/')

    messages.error(request, "Incorrect login credentials.")
    return HttpResponseRedirect('/')


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect('/')


def register(request):
    form = forms.registerForm()

    if request.method == 'POST':
        import ipdb; ipdb.set_trace()

    context = {
        'form': form,
    }
    return render(request, 'profiles/register.html', context)
