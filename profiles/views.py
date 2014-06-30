from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.models import User, Group
from profiles.models import UserProfile, GroupProfile

def view_user(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        user_profile = user.userprofile
    except User.DoesNotExist:
        raise Http404()

    context = {
        'user': user,
        'user_profile': user_profile
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
