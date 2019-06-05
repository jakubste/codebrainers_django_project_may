from django.core.mail import send_mail
from django.db.models.signals import pre_save
from django.dispatch.dispatcher import receiver
from django.template.loader import render_to_string

from wykop.accounts.models import User


@receiver(pre_save, sender=User)
def notify_user_about_ban(instance, **kwargs):
    if not instance.pk:
        return
    prev = User.objects.get(pk=instance.pk)

    if not prev.banned and instance.banned:
        send_mail(
            'Zbanowano Cię',
            render_to_string('accounts/emails/ban.txt', {'user': prev}),
            'noreply@moj-wykop.pl',
            [prev.email],
            fail_silently=False,
            html_message=render_to_string('accounts/emails/ban.html', {'user': prev}),
        )
    if prev.banned and not instance.banned:
        send_mail(
            'Odbanowano Cię',
            render_to_string('accounts/emails/unban.txt', {'user': prev}),
            'noreply@moj-wykop.pl',
            [prev.email],
            fail_silently=False,
            html_message=render_to_string('accounts/emails/unban.html', {'user': prev}),
        )
