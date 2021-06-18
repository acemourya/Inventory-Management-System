from django.urls import path
from .views import (
    index,
    laptops_view,
    desktops_view,
    mobiles_view,

    add_laptops,
    add_desktops,
    add_mobiles,

    edit_laptop,
    edit_desktop,
    edit_mobile,

    delete_laptop,
    delete_desktop,
    delete_mobile,
)

app_name = 'product'
urlpatterns = [
    path('', index, name='index'),
    path('laptops/', laptops_view, name="display_laptops"),
    path('desktops/', desktops_view, name="display_desktops"),
    path('mobiles/', mobiles_view, name="display_mobiles"),

    path('laptops/add_laptops/', add_laptops, name="add_product"),
    path('desktops/add_desktops/', add_desktops, name="add_product"),
    path('mobiles/add_mobiles/', add_mobiles, name="add_product"),

    path('laptops/edit_item/<int:id>/', edit_laptop, name="edit_laptop"),
    path('desktops/edit_item/<int:id>/', edit_desktop, name="edit_desktop"),
    path('mobiles/edit_item/<int:id>/', edit_mobile, name="edit_mobile"),

    path('laptops/delete/<int:id>/', delete_laptop, name="edit_laptop"),
    path('desktops/delete/<int:id>/', delete_desktop, name="edit_desktop"),
    path('mobiles/delete/<int:id>/', delete_mobile, name="edit_mobile"),
]
