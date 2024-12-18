from django import forms
from .models import ContactUs
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

# Form based on contactUs model
class ContactUsForm(forms.ModelForm):
    captcha = ReCaptchaField(
        widget=ReCaptchaV2Checkbox(attrs={
            'data-theme': 'light',  # Optional: adjust as needed
        })
    )

    class Meta:
        model = ContactUs
        labels = {"name": "", "email": "", "message": ""}
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'First and Last Name',
                'class': 'form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-sky-600 focus:outline-none',
            }),
            'email': forms.TextInput(attrs={
                'placeholder': 'Email address, we\'ll never share your email.',
                'class': 'form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-sky-600 focus:outline-none',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Leave a comment or send a message to inquire about future work.',
                'class': 'form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-sky-600 focus:outline-none',
                'rows': '3',
            }),
        }
        fields = '__all__'
