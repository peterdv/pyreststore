.. -*- coding: utf-8; mode: rst; -*-
.. Pyreststore introduction https://github.com/peterdv/pyreststore

.. To be able to generate PDF files, install the texlive-latex-extra package

.. For the Python documentation, 
   this convention is used which you may follow:
    • # with overline, for parts
    • * with overline, for chapters
    • =, for sections
    • -, for subsections
    • ^, for subsubsections
    • ", for paragraphs

.. image:: https://travis-ci.org/peterdv/pyreststore.svg?branch=master
    :target: https://travis-ci.org/peterdv/pyreststore
.. image:: https://img.shields.io/pypi/v/pyreststore.svg
    :target: https://pypi.python.org/pypi/pyreststore


Python implementation of a REST based storage
=============================================

`Pyreststore`_ is a `Python`_ implementation of a `REST`_ based storage, 
a web application capable of storing bitbuckets serialized as plain text. 
This is a varation of the `pastebin type`_ web applications implemented in
`Python`_ on top of `Django`_ and the associated `Django REST framework`_.

.. _`Pyreststore`: https://github.com/peterdv/pyreststore
.. _`Python`: https://www.python.org/
.. _`REST`: https://en.wikipedia.org/wiki/Representational_state_transfer
.. _`pastebin type`: https://en.wikipedia.org/wiki/Pastebin
.. _`Django`: https://www.djangoproject.com/
.. _`Django REST framework`: http://tomchristie.github.io/django-rest-framework/


Requirements
------------

* `Python`_ (2.7)
* `Django`_ (1.7, 1.8)
* `Django REST framework`_ (2.3.8+)
* `REST framework JWT Auth`_ (1.6)

.. _`REST framework JWT Auth`: https://github.com/GetBlimp/django-rest-framework-jwt

And the requirements inherited from these packages.

The distributed version pulls a number of optional packages 
such as for example
`swagger`_ (online inspection and documention of the api). 
These can be disabled by modifying the configuration 
and the calls in the code.

.. _`swagger`: https://github.com/marcgibbons/django-rest-swagger


Bugs & Contributions
--------------------

Please report bugs by opening an issue on github.

Contributions are welcome !


Background
----------

Plenty of fine pastebin applications exist, so why create yet another one ?
The answer is quite simply: because I could.
Professionally I found myself in need of an 
enterprise level, internal pastebin service, 
and none of the existing ones I considered did quite fit the bill. 
This, in combination with a summer vacation cumming up, 
made the decission to roll my own - 
and dig into Django along the way - an easy decission.

So pyreststore is used to fill a very specific need we had 
in our systems landscape, 
and at the same time it is a personal learning experience for me.
The implementation is inspired of my starting points learning about 
Django and Rest: The excelent `Django REST framwork Tutorial`_
and `Django Tutorial`_, 
without those I would not have embarked on this journey. 

.. _`Django REST framwork Tutorial`: http://tomchristie.github.io/django-rest-framework/#tutorial
.. _`Django Tutorial`: https://docs.djangoproject.com/en/1.8/intro/tutorial01/

If You consider using this code, please remember that it was implemented 
specifically for the two purposes stated above. 
You should carefully consider which support level You need, 
adopting this code implies that You will maintain the code yourself !
If You are capable and willing to do this, please dig in - and consider 
contributing here.
We have a single enterprise deployment of a slightly adapted version of 
pyreststore, but I do not have ressources to support pyreststore in general.

If You decide to go ahead, please read the `License` file, 
it should be wide enough to fit most purposes, 
and consult the `installation` notes.

.. _`License`: ./LICENSE
.. _`installation`: doc/installation.rst

I sincerely hope that You have as much fun as I have had !

`Peter Dahl Vestergaard`_

.. _`Peter Dahl Vestergaard`: https://dk.linkedin.com/in/peterdahlvestergaard


.. EOF
