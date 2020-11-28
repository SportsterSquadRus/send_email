from django.core.mail import send_mail
from send_email.passwords import email_pass


def send(user_email):
    send_mail(
        'some_text',
        'another_text',
        email_pass()[0],
        [user_email],
        fail_silently=True
    )
