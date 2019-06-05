from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'wykop.accounts'
    verbose_name = 'Accounts'

    def ready(self):
        import wykop.accounts.signals
