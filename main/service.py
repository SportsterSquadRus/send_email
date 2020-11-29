"""Send mail services"""
from django.core.mail import send_mail
from send_email.passwords import email_pass


def send(user_email):
    """first func for mail send"""
    send_mail(
        'some_text',
        'another_text',
        email_pass()[0],
        [user_email],
        fail_silently=True
    )

def send_beat(user_email):
    """second func for mail send"""
    send_mail(
        'some_beat_text',
        'another_beat_text',
        email_pass()[0],
        [user_email],
        fail_silently=True
    )
