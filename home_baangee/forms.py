from django import forms
from .models import Message
from nocaptcha_recaptcha.fields import NoReCaptchaField


class MessageForm(forms.ModelForm):
    name = forms.CharField(
        max_length=70,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Name"}),
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Email"})
    )
    captcha = NoReCaptchaField(error_messages={"required": "This check is mandatory."})

    class Meta:
        model = Message
        fields = ["name", "message", "email"]
        widgets = {
            "message": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Message"}
            ),
        }
