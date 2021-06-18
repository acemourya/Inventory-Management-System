from django.db.models import Q
from django.contrib import messages
from .models import Laptops, Desktops, Mobiles
from .forms import LaptopForm, DesktopForm, MobileForm
from django.shortcuts import render, redirect, get_object_or_404


def index(request):
    # Send on laptops list page

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
    return render(request, "product/index.html", context)


def laptops_view(request, *args, **kwargs):
    # View all laptop items

    return search(request, Laptops, "Laptops")


def desktops_view(request, *args, **kwargs):
    # View all desktop items

    return search(request, Desktops, "Desktops")


def mobiles_view(request, *args, **kwargs):
    # View all mobile items

    return search(request, Mobiles, "Mobiles")


def add_items(request, header, cls):
    # Add different items in diffrent models

    if request.method == "POST":
        form = cls(request.POST)

        # Check all fields is valid or not
        if form.is_valid():

            # Save all form fields data in databse
            form.save()
            return redirect("../")
    else:

        # Move forword on forms
        form = cls()
        context = {"form": form, "header": header}
        return render(request, "product/add_item.html", context)


def add_laptops(request):
    # Add laptop item

    return add_items(request, "Laptop", LaptopForm)


def add_desktops(request):
    # Add desktop item

    return add_items(request, "Desktop", DesktopForm)


def add_mobiles(request):
    # Add mobiles item

    return add_items(request, "Mobile", MobileForm)


def edit_item(request, id, header, model, cls):
    # Edit details of different items

    # Check the 'id' of item in database
    item = get_object_or_404(model, id=id)

    if request.method == "POST":

        """Open update form of item and initialise
        data of item in form fields"""
        form = cls(request.POST, instance=item)

        # Check form valid
        if form.is_valid():

            # Save item form data in database
            form.save()
            return redirect("../../")
    else:
        # Move forword to edit form if item
        form = cls(instance=item)
        return render(
            request, "product/edit_item.html", {"form": form, "header": header}
        )


def edit_laptop(request, id):
    # Edit laptop item data

    return edit_item(request, id, "Laptop", Laptops, LaptopForm)


def edit_desktop(request, id):
    # Edit desktop item data

    return edit_item(request, id, "Desktop", Desktops, DesktopForm)


def edit_mobile(request, id):
    # Edit mobile item data

    return edit_item(request, id, "Mobile", Mobiles, MobileForm)


def delete_item(request, id, model):
    # Delete item from database

    # Check the 'id' of item in database
    obj = get_object_or_404(model, id=id)

    if obj is not None:
        # Delete item from databse
        obj.delete()
        return redirect("../../")

    return redirect(".")


def delete_laptop(request, id):
    # Delete a laptop item from database
    return delete_item(request, id, Laptops)


def delete_desktop(request, id):
    # Delete a dektop item from database

    return delete_item(request, id, Desktops)


def delete_mobile(request, id):
    # Delete a mobile item from database

    return delete_item(request, id, Mobiles)
