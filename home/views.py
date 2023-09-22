from django.shortcuts import render
from django.core.mail import mail_admins
from .forms import ContactUs
from honeypot.decorators import check_honeypot

app_name='home'
@check_honeypot
def home(request):
    if request.POST:
        f = ContactUs(request.POST)
        if f.is_valid():

            human = True
            name = f.cleaned_data['name']
            sender = f.cleaned_data['email']
            subject = "Kevinpwhite.com | New Contact Form Submited {}:{}".format(name, sender)

            message = "Name: " + name + "\nsender: " + sender + "\n\nMessage: " + f.cleaned_data['message']
            mail_admins(subject, message)

            f.save()
            note = "Email sent and form submited successfully!"
            return render(request, 'home.html', {'form': ContactUs, 'note': note})
        else:
            failnote = "Sorry something failed please resubmit your form."
            return render(request, 'home.html', {'form': f, 'failnote':failnote})
    else:
        f = ContactUs()
        return render(request, 'home.html', {'form': f})

def links(request):
    return render(request, 'links.html')
