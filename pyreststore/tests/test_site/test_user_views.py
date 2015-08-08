# -*- coding: utf-8; mode: Python; -*-
from __future__ import unicode_literals

# Get an instance of a logger
import logging
import json
import django
from rest_framework import status
from rest_framework.reverse import reverse
from tests.baseTestCase import BaseTestCaseJWT
from tests.test_bckt.utils import create_bckt
from distutils.version import StrictVersion

logger = logging.getLogger(__name__)


class UserViewsTest(BaseTestCaseJWT):
    '''
    Unit tests for the user views
    '''

    def setUp(self):
        return super(UserViewsTest, self).setUp()

    def tearDown(self):
        return super(UserViewsTest, self).tearDown()

    def test_get_user_list(self):
        '''
        User views: GET user list
        '''

        url = reverse('user-list')
        print '{0!s}: url = "{1!s}"'.format(__name__, url)
        response = self.api_client.get(url)
        print '{0!s}: response.data: {1!s}'.format(__name__, response.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        if 'resolver_match' in dir(response):
            self.assertEqual(response.resolver_match.func.__name__,
                             'UserViewSet')
        if StrictVersion('1.8') <= StrictVersion(django.get_version()):
            self.assertEqual(response.charset, 'utf-8')
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertIn('GET', response['Allow'])
        self.assertNotIn('POST', response['Allow'])
        self.assertIn('HEAD', response['Allow'])
        self.assertIn('OPTIONS', response['Allow'])

    def test_get_user_detail(self):
        '''
        User views: GET user detail
        '''

        userUrl = reverse('user-list')
        url = ''.join([userUrl, unicode(self.testuserdata['pk']), '/'])
        print '{0!s}: url = "{1!s}"'.format(__name__, url)
        response = self.api_client.get(url)
        print '{0!s}: response = \n"""\n{1!s}\n"""'.format(__name__, response)
        print '{0!s}: response.data = {1!s}'.format(__name__, response.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        if 'resolver_match' in dir(response):
            self.assertEqual(response.resolver_match.func.__name__,
                             'UserViewSet')
        if StrictVersion('1.8') <= StrictVersion(django.get_version()):
            self.assertEqual(response.charset, 'utf-8')
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(response.data['username'],
                         self.testuserdata['username'])
        self.assertIn('GET', response['Allow'])
        self.assertNotIn('POST', response['Allow'])
        self.assertIn('HEAD', response['Allow'])
        self.assertIn('OPTIONS', response['Allow'])
