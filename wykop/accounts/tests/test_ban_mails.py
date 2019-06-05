from django.core import mail
from django.test import TestCase

from wykop.accounts.models import User


class BanMailTestCase(TestCase):

    def test_user_created_unbanned(self):
        user = User.objects.create(
            username='test-user',
            email='test@example.com',
        )
        self.assertFalse(user.banned)
        self.assertEqual(user.username, 'test-user')

        user.banned = True
        user.save()

        self.assertEqual(len(mail.outbox), 1)

        user.banned = False
        user.save()

        self.assertEqual(len(mail.outbox), 2)

        self.assertIn('Zbanowano', mail.outbox[0].subject)
        self.assertIn('Odbanowano', mail.outbox[1].subject)
