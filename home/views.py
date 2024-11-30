from django.shortcuts import render
from django.core.mail import mail_admins
from .forms import ContactUsForm
from honeypot.decorators import check_honeypot

app_name='home'
@check_honeypot
def home(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)  # Use the updated form
        if form.is_valid():
            name = form.cleaned_data['name']
            sender = form.cleaned_data['email']
            subject = f"Kevinpwhite.com | New Contact Form Submitted {name}:{sender}"

            message = f"Name: {name}\nSender: {sender}\n\nMessage: {form.cleaned_data['message']}"
            mail_admins(subject, message)

            form.save()
            note = "Email sent and form submitted successfully!"
            return render(request, 'home.html', {
                'form': ContactUsForm(),  # Render a fresh form
                'note': note,
            })
        else:
            failnote = "Sorry, something failed. Please resubmit your form."
            return render(request, 'home.html', {
                'form': form,  # Return form with errors
                'failnote': failnote,
            })
    else:
        form = ContactUsForm()  # Instantiate a new form
        return render(request, 'home.html', {'form': form})

def links(request):
    return render(request, 'links.html')
