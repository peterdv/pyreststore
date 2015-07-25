.. -*- coding: utf-8; mode: rst; -*-
.. pyreststore

.. To be able to generate PDF files, install the texlive-latex-extra package

.. For the Python documentation, 
   this convention is used which you may follow:
    • # with overline, for parts
    • * with overline, for chapters
    • =, for sections
    • -, for subsections
    • ^, for subsubsections
    • ", for paragraphs


README
======

.. Bibliographic fields:

:Authors: Peter Dahl Vestergaard
:Status: Work In Progress.
:Version: 0.01.001
:Date: 20150725


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

Plenty of fine pastebin applications exist, so why create yet another one ?
The answer is quite simply: because I could.
Professionally I found myself in need of an enterprise level pastebin service, 
and none of the existing ones I considered did quite fit the bill. 
This, in combination with a summer vacation cumming up, 
made the decission to roll my own - 
and dig into Django along the way - an easy decission.

So pyreststore is used to fill a very specic need we had 
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
We have a single enterprise deployment of a slightly adapted version of 
pyreststore, but we do not have ressources to support pyreststore in general.

If You decide to go ahead, please read the ``LICENSE`` file, 
it should be wide enough to fit most purposes.

I sincerely hope that You have as much fun as I have had !

`Peter Dahl Vestergaard`_

.. _`Peter Dahl Vestergaard`: https://dk.linkedin.com/in/peterdahlvestergaard


Preparing a working development directory
-----------------------------------------

This git repository only contains the appliction code, a number of 
supporting modules are needed to do any usefull work.

To do any development or production I recommend that you use:

#. An isolated Python environment based on 
   `virtualenv`_. 

#. A local `Django`_ installation 
   in the isolated Python environment.

#. A number of Python packages as documented in ``requirements.txt``.

.. _`virtualenv`: https://virtualenv.pypa.io/


Preparing an isolated Python instance using virtualenv
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

One common problem with installing packages directly to your 
current site-packages area is that, 
you both often have more than one project 
and often use Python on your machine for things other than Django. 
In either of these cases, you may run into dependency issues between your 
applications and the installed packages. 
For this reason, I am using virtualenv to manage 
an isolated Python installation, containing a local Django installation. 
This is common, and recommended, practice among Python and Django users.

After installing virtualenv in the operating system in whatever way you want, 
create a new isolated Python instance 
in the root directory of this repository, 
called ``pyreststoreEnv`` (named after the repository), 
using the following::

  $ virtualenv pyreststoreEnv

This creates a new subdirectory ``./pyreststoreEnv`` containing 
the isolated Python instance.

As You may be on a different operating system and/or 
a different Python version, 
this directory is excluded from the git repository - by listing it
in the ``.gitignore`` file, 
also located in the root directory of this repository.

Prior to performing anything, we need to *activate* the 
isolated Python instance by::

  $ source ./pyreststoreEnv/bin/activate

This sets up various environment variables 
to effectively bypass the system's Python install 
and uses the local pyreststoreEnv one instead.
 
You should see ``(pyreststoreEnv)$`` at Your prompt, 
letting you know that you're running under the 
virtualenv install. At any time, just type::

  (pyreststoreEnv)$ deactivate

to stop using virtualenv, 
returning to the default operating system Python instance.


Installing Django
^^^^^^^^^^^^^^^^^

I recommend using an installation of `Django`_ 
managed by virtualenv that can't be messed up by other users (or yourself) 
working elsewhere on the machine. 

To install Django under virtualenv, just type::

  (pyreststoreEnv)$ pip install django

This should give you the latest version of Django 
which will be installed in your virtualenv area. 
You can confirm this by doing::

  (pyreststoreEnv)$ which django-admin.py

Which should report an area under our ``pyreststoreEnv`` directory
(which is already excluded from this git repository, remember ?).

Python package requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The python package requirements are documented in ``./requirements.txt``.
To install the required Python packages using `pip`_, simply run::

  (pyreststoreEnv)$ pip install -r requirements.txt

This will also give You the Django installation described above.

.. _`pip`: https://pip.pypa.io/

.. EOF
