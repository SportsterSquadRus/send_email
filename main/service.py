"""Send mail services"""
from django.core.mail import send_mail
from send_email.passwords import email_pass


def send(user_email, text1, text2):
    send_mail(
        text1,
        text2,
        email_pass()[0],
        [user_email],
        fail_silently=True
    )


def send_once(user_email):
    """first func for mail send"""
    send('some_text', 'another_text', user_email)


def send_beat(user_email):
    """second func for mail send"""
    send('some_beat_text', 'another_text_beat', user_email)
