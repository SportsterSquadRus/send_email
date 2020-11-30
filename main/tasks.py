"""celery tasks"""
from send_email.celery import app
from .service import send_beat, send_once
from .models import Contact

# celery -A send_spam_email -l info
@app.task
def send_spam_email(user_email):
    """spam task"""
    send_once(user_email)

# celery -A send_email beat -l info
@app.task
def send_beat_email():
    """send mail every 2 mins"""
    for contact in Contact.objects.all():
        send_beat(contact.email)
