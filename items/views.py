from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.db import models
from items.models import Item
from items import forms


# @login_required(login_url='/admin')
def index(request):
    user = request.user

    # If user is logged in and it's not anonymous get items with his vision power.
    if not user.is_anonymous and user.userprofile:
        items = Item.objects.filter(active=True, vision_power__lte=user.userprofile.vision_power)
    else:
        items = Item.published.all()

    context = {
        'items': items,
    }
    return render(request, 'items/index.html', context)


def view_item(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)
    except (Item.DoesNotExist, Item.MultipleObjectsReturned):
        raise Http404()

    context = {}
    # Check if user have expected vision power
    if item.vision_power > settings.VISION_POWER:
        if request.user.userprofile and item.vision_power <= request.user.userprofile:
                context['item'] = item
        else:
            context['error'] = "You don't have permission to view this item."
    else:
        context['item'] = item

    return render(request, 'items/view.html', context)


def reserve_item(request, item_id):

    if request.method == 'POST' and request.user:
        try:
            item = Item.objects.get(item_id)
        except Item.DoesNotExist:
            raise Http404()

        user = request.user.userprofile
        form = forms.ReserveItem(request.POST)

        user.rent_item(item, form.reserve_to)

        return HttpResponseRedirect('/')
    else:
        form = forms.ReserveItem()
        try:
            item = Item.objects.get(pk=item_id)
        except (Item.DoesNotExist, Item.MultipleObjectsReturned):
                raise Http404()

        context = {
            'item': item,
            'form': form
        }
        return render(request, 'items/reserve.html', context)
