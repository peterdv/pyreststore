# -*- coding: utf-8; mode: Python; -*-
from __future__ import unicode_literals

import logging
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.reverse import reverse

logger = logging.getLogger(__name__)


class SiteLoginTest(TestCase):
    "Unit tests for site login"

    def setUp(self):
        self.user = User.objects.create_user('BcktTestUser',
                                             password=make_password('test'))

    def tearDown(self):
        self.user.delete()

    def test_display_login_dialog_plain(self):
        "Site login: GET login dialog (statuscode, function and Content-Type)"

        url = reverse('admin:login')
        logger.debug('reverse(\'admin:login\')  = %s' % url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.resolver_match.func.__name__, 'login')
        self.assertEqual(response['Content-Type'], 'text/html; charset=utf-8')
