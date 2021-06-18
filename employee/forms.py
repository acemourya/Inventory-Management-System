from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create forms here.
class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email")
