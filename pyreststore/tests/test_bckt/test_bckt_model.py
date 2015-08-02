# -*- coding: utf-8; mode: Python; -*-
from __future__ import unicode_literals

import json
from django.test import TestCase
from bckt.models import Bckt
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from tests.test_bckt.utils import create_bckt


class BcktTest(TestCase):
    '''
    Unit tests for the Bckt Django model
    '''

    def setUp(self):
        self.user = User.objects.create_user('BcktTestUser',
                                             password=make_password('test'))

    def tearDown(self):
        self.user.delete()

    def test_bckt_creation(self):
        '''
        Bckt model: Creation of a Bckt instance.
        '''

        title = 'Title: Created by test_bckt_creation()'
        contents = 'This is a two line content\nJust to check a newline'

        b = Bckt()
        b = create_bckt(user=self.user, title=title, contents=contents)
        self.assertTrue(isinstance(b, Bckt))
        self.assertEqual(b.title, title)
        self.assertEqual(b.code, contents)

    def test_bckt_creation_da(self):
        '''
        Bckt model: Use Danish national characters.
        '''

        title = 'Title: Created by test_bckt_creation() æøå ÆØÅ'
        contents = '''This is a 3 line content
Just to check a newline
and Danish national characters æøåÆØÅ'''

        b = create_bckt(user=self.user, title=title, contents=contents)
        self.assertTrue(isinstance(b, Bckt))
        self.assertEqual(b.title, title)
        self.assertEqual(b.code, contents)

    def test_assert_jsonLoads_improperjson(self):
        '''
        Bckt model: Assert that json.loads() reports illegal json string.
        '''

        # Illegal json syntax, control characters *within* a string literal
        # in the json data should be escaped.
        c_err = '''{"code": "Notes\n\nover 3 lines"}'''
        c = '''{"code": "Notes\\n\\nover 3 lines"}'''
        self.assertRaises(ValueError, json.loads, c_err)

    def test_assert_jsonLoads(self):
        '''
        Bckt model: Assert that json.loads() works as expected if strict=True
        '''

        # Illegal json syntax, control characters *within* a string literal
        # in the json data should be escaped as in:
        #    c = 'Notes\\n\\nover 3 lines'
        c = 'Notes\n\nover 3 lines'
        b1_py = {
            'title': 'Assert json.loads() test data',
            'language': 'Text',
            'code': c,
        }

        b1_json = '''{
        "title": "Assert json.loads() test data",
        "code": "Notes\\n\\nover 3 lines",
        "language": "Text"
        }
        '''
        print(b1_json)
        b1 = json.loads(b1_json)
        self.assertEqual(b1['title'], b1_py['title'])
        self.assertEqual(b1['language'], b1_py['language'])
        self.assertEqual(b1['code'], c)

    def test_assert_jsonLoads_relaxed(self):
        '''
        Bckt model: Assert that json.loads() works as expected if strict=False
        '''

        # Illegal json syntax, control characters *within* a string literal
        # in the json data should be escaped as in:
        #    c = 'Notes\\n\\nover 3 lines'
        c = 'Notes\n\nover 3 lines'
        b1_py = {
            'title': 'Assert json.loads() test data',
            'language': 'Text',
            'code': c,
        }

        b1_json = '''{
        "title": "Assert json.loads() test data",
        "code": "Notes

over 3 lines",
        "language": "Text"
        }
        '''

        b1 = json.loads(b1_json, strict=False)
        self.assertEqual(b1['title'], b1_py['title'])
        self.assertEqual(b1['language'], b1_py['language'])
        self.assertEqual(b1['code'], c)

    def test_bckt_creation_from_json(self):
        '''
        Bckt model: Creation of a Bckt instance from a json string.
        '''

        b1_json = '''
{
"title": "Title: Created by test_bckt_creation_from_json()",
"code":
"Danish national characters \\n such as æøåÆØÅ\\n might pose a problem",
"language": "Text"
}
'''
        print(b1_json)
        b1 = json.loads(b1_json, strict=True)

        b = create_bckt(user=self.user, jsonBckt=b1_json)
        print(type(b))
        self.assertTrue(isinstance(b, Bckt))
        self.assertEqual(b.title, b1['title'])
        self.assertEqual(b.language, b1['language'])
        self.assertEqual(b.code, b1['code'])

    def test_bckt_creation_max_bckts_limit(self):
        '''
        Bckt model: Enforcement of PYRESTSTORE_MAX_BCKTS on creation.
        '''

        from django.conf import settings

        def mktitle(n, n_max):
            s = 'Test bucket number {:d} of {:d}'.format(n, n_max)
            return s

        n_max = settings.PYRESTSTORE_MAX_BCKTS
        print('PYRESTSTORE_MAX_BCKTS = {!s}'.format(n_max))
        # Overshoot by 2
        for n in xrange(0, n_max + 2):
            title = mktitle(n, n_max)
            code = ''.join([
                'We should *never* see more than ',
                ' {:d} \n'.format(n_max),
                'concurrent buckets persisted in the database. \n\n',
                'When this limit is reached, creation of the ',
                'next bucket\n',
                'is expected to result in the deletion of the oldest\n',
                '\n\nThis is bucket number {:d}'.format(n)
            ])
            data = {'title': title, 'code': code, 'language': 'Text'}
            b = create_bckt(user=self.user, jsonBckt=json.dumps(data))

        # Get the current Bckt instances in the database
        bckts = Bckt.objects.all()

        self.assertEqual(len(bckts), settings.PYRESTSTORE_MAX_BCKTS)
        for n in xrange(0, n_max):
            e_title = mktitle(n + 2, n_max)
            print('Expect title ', e_title)
            self.assertEqual(e_title, bckts[n].title)
