from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.cache import cache


@shared_task(name='send email with code')
def send_email_with_code(to: str, code: str, email_type: str, host: str):
    from_mail = 'codeportalproject@gmail.com'
    subject = 'Código de confirmação do email'
    html_message = render_to_string('emails/code.html', {'code': code, 'host': host})
    plain_message = strip_tags(html_message)
    send_mail(subject, f'Código de verificação: {code}', from_mail, [to], html_message=html_message)
    return {'email_to': to, 'type': email_type}



@shared_task(name='send email for create new password')
def send_email_for_create_new_password(to: str, token: str, host: str):
    cache.set(f'create_new_password_to_{to}', {'token': token}, 60*10)
    from_mail = 'codeportalproject@gmail.com'
    subject = 'Link para criar nova senha'
    html_message = render_to_string('emails/create_new_password.html', {'token': token, 'email': to, 'host': host})
    plain_message = strip_tags(html_message)
    send_mail(subject, 'Acesse o link para terminar o processo', from_mail, [to], html_message=html_message)
    return {'email_to': to, 'type': 'create new password'}