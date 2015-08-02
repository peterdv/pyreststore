# -*- coding: utf-8; mode: Python; -*-
from __future__ import unicode_literals

import logging
from django.test import TestCase
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework_jwt.utils import jwt_decode_handler

logger = logging.getLogger(__name__)


class BaseTestCaseJWT(TestCase):
    '''
    Extending django.test.TestCase

    '''

    def setUp(self):
        '''
        Create data and other attributes usefull in tests:

        api_client
        An instance of rest_framework.test.APIClient().

        testuserdata
        Data for a test user.

        testUser
        An instance of django.contrib.auth.models.User reprecenting
        the testuser created based on self.testuserdata.

        data
        Data usefull for authenticating testUser.
        '''

        self.api_client = APIClient()
        self.testuserdata = {}
        self.testuserdata['username'] = 'JWTbasedTestUser'
        self.testuserdata['password'] = 'test'
        self.testuserdata['passwordHash'] = \
            make_password(self.testuserdata['password'])
        self.testuserdata['email'] = 'email@gmail.com'
        self.testuserdata['pk'] = None
        self.testuserdata['jwtToken'] = None
        self.testUser = User.objects.create_user(
            self.testuserdata['username'],
            email=self.testuserdata['email'],
            password=self.testuserdata['password']
        )
        self.testuserdata['pk'] = self.testUser.pk
        self.testUser.save()
        print '{0!s}: testUser.pk       = "{1!s}"'.format(
            __name__,
            self.testUser.pk
        )
        print '{0!s}: testUser.username = "{1!s}"'.format(
            __name__,
            self.testUser.username
        )
        print '{0!s}: testUser.password = "{1!s}"'.format(
            __name__,
            self.testUser.password
        )

        self.data = {
            'username': self.testuserdata['username'],
            'password': self.testuserdata['password']
        }
        self.testuserJwtLogin()

    def testuserJwtLogin(self):
        '''
        Authenticate a user, and prepare JWT token based authentification.

        POST user credentials to the JWT login url using the default
        django.test.TestCase.Client client.

        Returns the HTTP status code from this POST.

        Capture the JWT token from the request response,
        store it in testuserdata['jwtToken']
        and setup the class method api_client() to authenticate
        using this JWT token.
        '''

        # https://docs.djangoproject.com/en/1.8/releases/1.8/:
        #   Passing a dotted path to reverse() and url
        #
        #   Reversing URLs by Python path is an expensive operation as it
        #   causes the path being reversed to be imported.
        #   This behavior has also resulted in a security issue.
        #   Use named URL patterns for reversing instead.
        #
        # See also:
        # https://docs.djangoproject.com/en/1.8/topics/auth/passwords/

        # url = reverse('rest_framework_jwt.views.obtain_jwt_token')
        url = reverse('jwt_token_auth')
        response = self.client.post(url, self.data, format='json')
        jwtToken = response.data['token']
        self.testuserdata['jwtToken'] = jwtToken
        self.testuserdata['decodedJwtToken'] = jwt_decode_handler(jwtToken)
        authHeader = 'JWT ' + self.testuserdata['jwtToken']
        self.api_client.credentials(HTTP_AUTHORIZATION=authHeader)
        return response.status_code

    def responseToDebugLog(self, resp, disp=False, log=None):
        v_fmt = '{!s} = {!s}'

        if log is None:
            log = logging.getLogger(__name__).debug

        m = v_fmt.format('response.status_code', resp.status_code)
        log(m)
        if disp:
            print(m)

        m = v_fmt.format(
            'response.data',
            resp.data
        )
        log(m)
        if disp:
            print(m)

        try:
            d = resp.content
        except:
            d = 'Not present'
        m = v_fmt.format(
            'response.content',
            d
        )
        log(m)
        if disp:
            print(m)
