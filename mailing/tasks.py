from celery import shared_task
from mailing.models import SetMessage
from mailing.services.services import finish_task, delete_task, send_mailing


@shared_task(name='send_message')
def send_message(mailing_id):
    mailing = SetMessage.objects.get(pk=mailing_id)
    if finish_task(mailing):
        delete_task(mailing)
        return
    return send_mailing(mailing)