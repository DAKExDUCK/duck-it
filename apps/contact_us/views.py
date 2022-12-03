import traceback
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import render, redirect
from contact_us.forms import ContactForm
from apps.main_app.settings import DEFAULT_FROM_EMAIL
from django.contrib.auth.models import User


def contactView(request: HttpRequest):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = f"{form.cleaned_data['message']}\n\nFrom E-mail: {from_email}\n"
            if request.user.is_authenticated:
                message += (f"Username: {request.user.username}\n"
                            f"E-mail: {User.objects.get(id=request.user.id).email}\n")
            try:
                send_mail(subject, message, DEFAULT_FROM_EMAIL, [DEFAULT_FROM_EMAIL])
            except Exception as exc:
                traceback.format_exc(exc)
                data = {
                    'status': "error",
                    'msg': "An error occurred while submitting the form!"
                }
            else:
                data = {
                    'status': "ok",
                    'msg': "Form submitted successfully!"
                }
            return render(request, "contact_us/done.html", data)
    return render(request, "contact_us/contact_us.html", {'form': form})