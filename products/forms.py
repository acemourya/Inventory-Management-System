from django import forms
from .models import Laptops, Desktops, Mobiles


class LaptopForm(forms.ModelForm):
    # Laptop form

    class Meta:
        model = Laptops
        fields = ("type", "price", "status", "issues")


class DesktopForm(forms.ModelForm):
    # Desktop form

    class Meta:
        model = Desktops
        fields = ("type", "price", "status", "issues")


class MobileForm(forms.ModelForm):
    # Mobile form

    class Meta:
        model = Mobiles
        fields = ("type", "price", "status", "issues")
