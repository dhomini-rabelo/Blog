from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags



@shared_task(name='send email with code')
def send_email_with_code(to: str, code: str, email_type: str):
    from_mail = 'codeportalproject@gmail.com'
    subject = 'Código de confirmação de email'
    html_message = render_to_string('emails/code.html', {'code': code})
    plain_message = strip_tags(html_message)
    send_mail(subject, plain_message, from_mail, [to], html_message=html_message)
    return {'email_to': to, 'type': email_type}