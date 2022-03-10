from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _


class SignUpForm(UserCreationForm):
    password2 = forms.CharField(
        label="Re-Password",  # show label name
        required=False,  # remove required attr
        # strip=False,                       # False mean accept backspace
        widget=forms.TextInput(
            attrs={
                "placeholder": "Employee Name",
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_first_name(self, *args, **kwargs):
        first_name = self.cleaned_data.get("first_name")
        if first_name == "":
            raise forms.ValidationError(_("first_name can not be blank"))
        else:
            return first_name
