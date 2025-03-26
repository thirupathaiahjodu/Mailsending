from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings
from .forms import ContactForm
from .models import Contact

def send_email_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            Contact.objects.create(name=name, email=email, message=message)
            send_mail(
                f"Message from {name}",
                message,
                email,
                [email],  
                fail_silently=False,
            )
            return render(request, 'success.html')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


