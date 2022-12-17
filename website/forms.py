from django import forms
from website.models import Contact


class contactform(forms.ModelForm):

    #captcha = CaptchaField()

    class Meta :
        model=Contact
        fields= '__all__'