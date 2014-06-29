from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from django.db import models
from items.models import Item

# Create your views here.
def index(request):
    items = Item.objects.all()

    template = loader.get_template('items/index.html')
    context = RequestContext(request, {
        'items': items,
        })
    return HttpResponse(template.render(context))
