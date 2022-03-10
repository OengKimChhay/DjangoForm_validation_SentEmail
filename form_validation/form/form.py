from django import forms
from .models import Employee
from django.utils.translation import gettext_lazy as _
import re

EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
SPECIAL_CHAR_REGEX = "[@_!#$%^&*()<>?/\|}{~:]"


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ('views',)  # exclude the views' column in form template

    name = forms.CharField(
        label="Employee Name",  # show label name
        label_suffix=" **",  # show next to label
        required=False,  # remove required attr
        # strip=False,                       # False mean accept backspace
        widget=forms.TextInput(
            attrs={
                "placeholder": "Employee Name",
                "class": "form-control"
            }
        )
    )

    email = forms.EmailField(
        label_suffix=" **",
        label="Email",
        required=False,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Example@gmail.com",
                "class": "form-control"
            }
        )
    )

    password = forms.CharField(
        label_suffix=" **",
        label="Password",
        required=False,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ),
        help_text="must contain special characters, more then 5 characters"
    )

    repassword = forms.CharField(
        label_suffix=" **",
        label="Re-Password",
        required=False,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Re-Password",
                "class": "form-control"
            }
        )
    )

    contact = forms.CharField(
        label_suffix=" **",
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Employee contact",
                "class": "form-control",
                "rows": "5"
            }
        )
    )

    # ----------- validation -----------------
    # ------------ the clean func is for global error not in the feilds form --------------------
    def clean(self):
        cleaned_data = super(EmployeeForm, self).clean()
        password = cleaned_data.get("password")
        repassword = cleaned_data.get("repassword")

        if password is not None:
            if password != repassword:
                raise forms.ValidationError(
                    "password and re-password does not match"
                )

    def clean_name(self, *args, **kwargs):
        name = self.cleaned_data.get("name")
        if name == "":
            raise forms.ValidationError(_("Employee Name can not be blank"))
        else:
            return name

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if email and not re.match(EMAIL_REGEX, email):
            raise forms.ValidationError(_('Invalid email format, example@gmail.com'))
        elif email == "":
            raise forms.ValidationError(_("Employee Email can not be blank"))
        else:
            return email

    def clean_password(self, *args, **kwargs):
        password = self.cleaned_data.get("password")
        name = self.cleaned_data.get("name")
        email = self.cleaned_data.get("email")
        if password == "":
            raise forms.ValidationError(_("Password can not be blank"))
        elif len(password) <= 5:
            raise forms.ValidationError(_("Password must be more then 5 characters"))
        elif password == name:
            raise forms.ValidationError(_("Password is too similar to the name"))
        elif password == email:
            raise forms.ValidationError(_("Password is too similar to the email"))
        elif password and not re.compile(SPECIAL_CHAR_REGEX).search(password):
            raise forms.ValidationError(_('Password must contain special characters'))
        else:
            return password

    def clean_contact(self, *args, **kwargs):
        contact = self.cleaned_data.get("contact")
        if contact == "":
            raise forms.ValidationError(_("Contact can not be blank"))
        else:
            return contact


class EmailForm(forms.Form):
    name = forms.CharField(
        label="Name",  # show label name
        label_suffix=":",  # show next to label
        required=False,  # remove required attr
        # strip=False,                       # False mean accept backspace
        widget=forms.TextInput(
            attrs={
                "placeholder": "Name",
                "class": "form-control"
            }
        )
    )

    email = forms.EmailField(
        label_suffix=":",
        label="Sent To Email",
        required=False,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Example@gmail.com",
                "class": "form-control"
            }
        )
    )
    contact = forms.CharField(
        label_suffix=":",
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "contact",
                "class": "form-control",
                "rows": "5"
            }
        )
    )

    def clean_name(self, *args, **kwargs):
        name = self.cleaned_data.get("name")
        if name == "":
            raise forms.ValidationError(_("Name can not be blank"))
        else:
            return name

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if email and not re.match(EMAIL_REGEX, email):
            raise forms.ValidationError(_('Invalid email format, example@gmail.com'))
        elif email == "":
            raise forms.ValidationError(_("Email can not be blank"))
        else:
            return email

    def clean_contact(self, *args, **kwargs):
        contact = self.cleaned_data.get("contact")
        if contact == "":
            raise forms.ValidationError(_("Contact can not be blank"))
        else:
            return contact
