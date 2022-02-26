from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


@shared_task(name='Enviando email')
def send_email_with_celery(to: str):
    from_mail = 'codeportalproject@gmail.com'
    subject = 'Código de confirmação de email'
    # html_message = render_to_string('mail.html', {'context': 'values'})
    # plain_message = strip_tags(html_message)
    send_mail(subject, 'sou um teste', from_mail, [to])
    # , html_message=html_message
    return {'email_to': to, 'type': 'register'}