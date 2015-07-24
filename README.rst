.. -*- coding: utf-8; mode: rst; -*-
.. pyreststore

.. To be able to generate PDF files, install the texlive-latex-extra package

.. For the Python documentation, 
   this convention is used which you may
   follow:
    • # with overline, for parts
    • * with overline, for chapters
    • =, for sections
    • -, for subsections
    • ^, for subsubsections
    • ", for paragraphs


README
======


Preparing a working development directory
-----------------------------------------

This git repository only contains the local code, a number of 
supporting modules are need to do any usefull work.

To do any development or production I recommend that you use:

#. An isolated Python environment based on 
   "virtualenv":https://virtualenv.pypa.io/. 

#. A local 
   Django:https://www.djangoproject.com/ 
   installation in the isolated Python environment.


Preparing an isolated Python instance using virtualenv
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

  $ deactivate

to stop using virtualenv, 
returning to the default operating system Python instance.


Installing Django
^^^^^^^^^^^^^^^^^

I recommend using an installation of 
Django:https://www.djangoproject.com/ 
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

.. EOF
