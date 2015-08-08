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
    """Base class for the testcases in this project.

    Provide general data and utility functions to the
    individual testcases.

    Attributes:

        `api_client` (:class:`rest_framework.test.APIClient`):
            Client to use in tests.
            Should not be modified directly.

        `testuserdata` (dict):
            Definition of the tesuser.

        `testUser` (:class:`django.contrib.auth.models.User`):
            The testuser created based on `testuserdata`.

        `data` (dict):
            Data usefull for authenticating testUser.
    """

    def setUp(self):
        """Initialize data and other attributes.
        """
        # Create a client to use in tests
        self.api_client = APIClient()
        # Initialize metadata about the test user to create
        self.testuserdata = {}
        self.testuserdata['username'] = 'JWTbasedTestUser'
        self.testuserdata['password'] = 'test'
        self.testuserdata['passwordHash'] = \
            make_password(self.testuserdata['password'])
        self.testuserdata['email'] = 'email@gmail.com'
        self.testuserdata['pk'] = None
        self.testuserdata['jwtToken'] = None
        # Create the testuser
        self.testUser = User.objects.create_user(
            self.testuserdata['username'],
            email=self.testuserdata['email'],
            password=self.testuserdata['password']
        )
        self.testuserdata['pk'] = self.testUser.pk
        # Persist the testuser
        self.testUser.save()
        # Dump some information
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
        # Initialize data to use in authentication
        self.data = {
            'username': self.testuserdata['username'],
            'password': self.testuserdata['password']
        }
        # Authenticate the test user, sets the JWT token
        self.testuserJwtLogin()

    def testuserJwtLogin(self):
        """Authenticate a test user, and prepare JWT token based authentification.

        POST user credentials to the JWT login url using the default
        :class:`django.test.TestCase.Client` client.

        Capture the JWT token from the request response,
        store it in :attr:`testuserdata['jwtToken']`,
        and setup the method :meth:`api_client()` of this instance
        to authenticate using this JWT token.

        Returns:
            The HTTP status code.
        """

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
        """
        Logs seleced information from the resonse object.

        Args:

            resp (:class:`rest_framework.response.Response`):
                The response object to log information from.

            disp (bool):
                If `True`, also print log information.

            log (:class:`loggig.Logger`):
                Logger to use, defaults to a local logger.
        """

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
