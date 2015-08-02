# -*- coding: utf-8; mode: Python; -*-
from __future__ import unicode_literals

import logging
from rest_framework import status
from rest_framework.reverse import reverse
from tests.baseTestCase import BaseTestCaseJWT

logger = logging.getLogger(__name__)


class SiteUrlLayoutTest(BaseTestCaseJWT):
    '''
    Unit tests for the URL layout of the site
    '''

    def setUp(self):
        return super(SiteUrlLayoutTest, self).setUp()

    def tearDown(self):
        return super(SiteUrlLayoutTest, self).tearDown()

    def test_jwt_login_post(self):
        '''
        Ensure JWT login view using JSON POST works.

        This will change the JWT token used in subsequent tests from the one
        initially created by steUp().
        '''

        status_code = self.testuserJwtLogin()

        self.assertEqual(status_code, status.HTTP_200_OK)
        self.assertEqual(self.testuserdata['decodedJwtToken']['username'],
                         self.testuserdata['username'])

    def test_get_api_root_plain(self):
        '''
        URL layout: GET api root
        '''

        url = reverse('api-root')
        response = self.api_client.get(url)
        print 'test_get_api_root_plain: response.data:', response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.resolver_match.func.__name__, 'APIRoot')
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertIn('Content-Type: application/json',
                      response.serialize_headers())
        self.assertIn('/bckt/', response.content)
        self.assertIn('/users/', response.content)
