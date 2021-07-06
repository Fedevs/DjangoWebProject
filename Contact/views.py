from django.shortcuts import redirect, render
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.

def contact(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            form_info = contact_form.cleaned_data

            try:
                send_mail('Contact Form from DjangoWebApp', form_info['message'], form_info.get('email', ''), ['yourEmail@gmail.com'])
                return redirect('/contact/?ok')

            except:
                return redirect('/contacto/?wrong')




    return render(request, 'Contact/contact.html', {'myForm': contact_form})
