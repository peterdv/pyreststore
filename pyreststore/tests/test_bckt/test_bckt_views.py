# -*- coding: utf-8; mode: Python; -*-
from __future__ import unicode_literals

import logging
import json
import django
from distutils.version import StrictVersion
from rest_framework import status
from rest_framework.reverse import reverse
from tests.baseTestCase import BaseTestCaseJWT
from tests.test_bckt.utils import create_bckt
from bckt.models import Bckt

logger = logging.getLogger(__name__)


class BcktViewsTest(BaseTestCaseJWT):
    '''
    Unit tests for the Bckt Django views
    '''

    def setUp(self):
        return super(BcktViewsTest, self).setUp()

    def tearDown(self):
        return super(BcktViewsTest, self).tearDown()

    def test_get_bcktList_plain(self):
        '''
        Bckt views: GET list of buckets
        '''

        url = reverse('bckt-list')
        logger.debug('reverse(\'bckt-list\')  = %s' % url)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        if 'resolver_match' in dir(response):
            self.assertEqual(response.resolver_match.func.__name__,
                             'BcktViewSet')
        if (django.VERSION >= (1, 8)):
            self.assertEqual(response.charset, 'utf-8')
        else:
            print('New in Django 1.8: response.charset')
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertIn('GET', response['Allow'])
        self.assertIn('POST', response['Allow'])
        self.assertIn('HEAD', response['Allow'])
        self.assertIn('OPTIONS', response['Allow'])

    def test_create_two_buckets_get_bckt_list(self):
        '''
        Bckt views: POST two buckets

        '''

        logger = logging.getLogger(str(__name__))
        logger.debug('Entry')
        url = reverse('bckt-list')
        logger.debug('reverse(\'bckt-list\')  = {:s}'.format(url))
        title = 'Bucket 1'
        code = 'Contents of Bucket 1.'
        data_0 = {'title': title, 'code': code, 'language': 'text'}
        title = 'Bucket 2'
        code = 'Contents of Bucket 2 \\nConsists of two lines.'
        data_1 = {'title': title, 'code': code, 'language': 'text'}

        response = self.api_client.post(url, data_0, format='json')
        self.responseToDebugLog(
            response, log=logger.debug
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        if 'resolver_match' in dir(response):
            self.assertEqual(response.resolver_match.func.__name__,
                             'BcktViewSet')

        response = self.api_client.post(url, data_1, format='json')
        self.responseToDebugLog(
            response,
            disp=True, log=logger.debug
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        if 'resolver_match' in dir(response):
            self.assertEqual(response.resolver_match.func.__name__,
                             'BcktViewSet')

        # Get the current Bckt instances in the database
        bckts = Bckt.objects.all()
        m = '{!s} = {!s}'.format(
            'len(bckts)',
            len(bckts)
        )
        logger.debug(m)

        self.assertEqual(2, len(bckts))
        self.assertEqual(data_0['title'], bckts[0].title)
        self.assertEqual(data_0['code'], bckts[0].code)
        self.assertEqual(data_1['title'], bckts[1].title)
        self.assertEqual(data_1['code'], bckts[1].code)
