from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.exceptions import SoftTimeLimitExceeded
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.cache import cache
from django.conf import settings

EMAIL_TASK_CONFIG = {
    'soft_time_limit': 20,
    'autoretry_for': (SoftTimeLimitExceeded,),
    'default_retry_delay': 15,
    'retry_backoff': True,
    'max_retry': 3,    
}

EMAIL = {
    'host': settings.DEFAULT_FROM_EMAIL,
}

@shared_task(name='send email with code', **EMAIL_TASK_CONFIG)
def send_email_with_code(to: str, code: str, email_type: str, host: str):
    subject = 'Código de confirmação do email'
    html_message = render_to_string('emails/code.html', {'code': code, 'host': host})
    send_mail(subject, f'Código de verificação: {code}', EMAIL['host'], [to], html_message=html_message)
    return {'email_to': to, 'type': email_type}



@shared_task(name='send email for create new password', **EMAIL_TASK_CONFIG)
def send_email_for_create_new_password(to: str, token: str, host: str):
    cache.set(f'create_new_password_to_{to}', {'token': token}, 60*10)
    subject = 'Link para criar nova senha'
    html_message = render_to_string('emails/create_new_password.html', {'token': token, 'email': to, 'host': host})
    send_mail(subject, 'Acesse o link para terminar o processo', EMAIL['host'], [to], html_message=html_message)
    return {'email_to': to, 'type': 'create new password'}