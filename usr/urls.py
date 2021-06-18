from django.urls import path
from .views import (
    index,
    laptops_view,
    desktops_view,
    mobiles_view,
)

app_name = "user"

# Define all urls path
urlpatterns = [
    path("", index, name="index"),
    path("laptops/", laptops_view, name="display_laptops"),
    path("desktops/", desktops_view, name="display_desktops"),
    path("mobiles/", mobiles_view, name="display_mobiles"),
]
