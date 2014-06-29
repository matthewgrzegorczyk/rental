from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.db import models
from items.models import Item

# @login_required(login_url='/admin')
def index(request):
    items = Item.objects.all()

    template = loader.get_template('items/index.html')
    context = RequestContext(request, {
        'items': items,
        })
    return HttpResponse(template.render(context))

def view_item(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)
    except (Item.DoesNotExist, Item.MultipleObjectsReturned):
        raise Http404()

    template = loader.get_template('items/view.html')
    context = RequestContext(request, {
        'item': item,
        })
    return HttpResponse(template.render(context))
