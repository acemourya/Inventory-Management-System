from django.contrib import admin
from .models import Laptops, Desktops, Mobiles


# Register models here.
@admin.register(Laptops, Desktops, Mobiles)
class DefaultAdmin(admin.ModelAdmin):
    """Add laptop, desktop, mobile model
    in admin panel"""

    pass
