import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Slika


# Create your views here.
def home(request):
    return render(request, "html/index.html")  # This looks for index.html in templates folder

def galerija(request):

    slike = Slika.objects.all()

    context = {"slike": slike}

    return render(request,"html/gallery.html",context)

def photos(request):
    return render(request, "html/photos.html")

def contact(request):

    email_sent = request.GET.get('email_sent', '')

    context = {
        'email_sent': email_sent
    }

    return render(request, "html/contact.html", context)

def about_us(request):
    return render(request, "html/about.html")


def send_email(request):
    name = request.POST.get("name", "")
    email = request.POST.get("email", "")
    phone = request.POST.get("phone", "")
    eventType = request.POST.get("eventType", "")
    message = request.POST.get("message", "")

    sender_email = "ivas.stranica@gmail.com"
    #Lozinka: Anaana123
    sender_password = "yuyf ijwn days musc"
    ivas_email = "ivas.stranica@gmail.com"

    # Confirmation email to the user
    user_subject = "Confirmation of Sent Message"
    user_body = f"""
                Dear {name},

                Your message has been successfully received. Here are the details of your request:

                Name: {name}
                Enauk: {email}
                Number: {phone}
                Event: {eventType}
                Message: {message}

                We will contact you soon.

                Sincerely,
                Ivas Group
                """

    # Notification email to salon
    ivas_subject = "Zaprimljena Nova Poruka sa Web Stranice"
    ivas_body = f"""
            Poštovani,

            Zaprimljena je nova poruka sa Stranice. Detalji:

            Ime: {name}
            Email: {email}
            Broj: {phone}
            Event: {eventType}
            Poruka: {message}

            """

    # Sending emails
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)

            # Send confirmation email to the user
            user_message = MIMEMultipart()
            user_message["From"] = sender_email
            user_message["To"] = email
            user_message["Subject"] = user_subject
            user_message.attach(MIMEText(user_body, "plain"))
            server.sendmail(sender_email, email, user_message.as_string())

            # Send notification email to the salon
            ivas_message = MIMEMultipart()
            ivas_message["From"] = sender_email
            ivas_message["To"] = ivas_email
            ivas_message["Subject"] = ivas_subject
            ivas_message.attach(MIMEText(ivas_body, "plain"))
            server.sendmail(sender_email, ivas_email, ivas_message.as_string())

        print("Emails sent successfully!")
        # Return with a flag indicating success
        return redirect(
            reverse(
                'contact') + f'?email_sent={True}'
        )
    except Exception as e:
        print(f"Error: {e}")
        return redirect(
            reverse(
                'contact')
        )
