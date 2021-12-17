# django
from django.utils.html import format_html


def success_message(message: str):
    success_message_html = f"""
    <div class="django-message success">
        <p><img src="/static/admin/img/icon-yes.svg" alt="success-img">{message}</p>
    </div>
    """

    return format_html(success_message_html)


def error_message(message: str):
    error_message_html = f"""
    <div class="django-message error">
        <p><img src="/static/admin/img/icon-no.svg" alt="error-img">{message}</p>
    </div>
    """

    return format_html(error_message_html)