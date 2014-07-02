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
    items = Item.objects.all()

    # template = loader.get_template('items/index.html')
    # context = RequestContext(request, {
    #     'items': items,
    #     })
    # return HttpResponse(template.render(context))
    context = {
        'items': items,
    }
    return render(request, 'items/index.html', context)


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


def reserve_item(request, item_id):

    if request.method == 'POST':

        form = forms.ReserveItem(request.POST)

        if form.is_valid:
            items = Item.objects.all()
            status = u"Item reserved successfully."

            context = {
                'items': items,
                'status': status,
            }

            return render(request, 'items/index.html', context)
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
