from django.shortcuts import (
    render,
    redirect,
)
from products.models import (
    Laptops,
    Desktops,
    Mobiles,
)
from django.db.models import Q
from django.contrib import messages


def index(request):
    # Move forword on laptop list page

    return redirect("./laptops")


def search(request, model, header):
    # Search item in database by Model name or type

    items = model.objects.all()

    # If user search item
    if request.method == "POST":
        srch = request.POST["srch"]
        if srch:
            items = model.objects.filter(
                    Q(id__iexact=srch) |
                    Q(type__istartswith=srch))
            if len(items) == 0:
                items = model.objects.all()
                messages.info(request, "No any item by this name")
        else:
            items = model.objects.all()
    
    context = {
        "items": items,
        "header": header,
    }
    return render(request, "usr/index.html", context)


def laptops_view(request, *args, **kwargs):
    # View all laptop items

    return search(request, Laptops, "Laptops")


def desktops_view(request, *args, **kwargs):
    # View all desktop items

    return search(request, Desktops, "Desktops")


def mobiles_view(request, *args, **kwargs):
    # View all mobile items

    return search(request, Mobiles, "Mobiles")
