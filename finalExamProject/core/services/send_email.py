from celery import shared_task
from services.ses import SESService


@shared_task
def send_notification_email(email, username):
    SESService().send_email(email=email, username=username)
