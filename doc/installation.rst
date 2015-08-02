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


Installation
============

This git repository only contains the appliction code, a number of 
supporting modules are needed to do any usefull work.

To do any development or production I recommend that you use the following 
procedure, which will enable You to contribute,
should You decide to do so::

#. Fork the `pyreststore repository on GitHub`_.

#. Clone your fork locally::

     $ git clone https://github.com/<your_username>/pyreststore.git
     $ cd pyreststore

#. `Prepare an isolated Python instance using virtualenv`_,
   and activate it.

#. `Install the Python package requirements`_  
   in the isolated Python environment, including Django.

#. `Customize the settings`_.

#. `Create the model`_.

#. `Create an admin user`_.

#. `Start pyreststore`_.


.. _`pyreststore repository on GitHub`: https://github.com/peterdv/pyreststore


Locating the intended ``pyreststore`` directory
-----------------------------------------------

I know, there are a lot of directories called ``pyreststore``, including 
the git repository itself - sorry ! I shall try to be very explicit when
referring to them:
 
- The git ``pyreststore`` directory itself on your disc
  (containing the ``README.rst`` file 
  and the ``pyreststoreEnv`` directory) 
  is referred to as ``./``. 

- The Django ``pyreststore`` project directory 
  (containing the ``manage.py`` file
  and yet another ``pyreststore`` directory 
  holding the Python package for this project,
  beeing the third directory in a row on Your disc having the same name).
  
  The Django project directory is referred to as ``./pyreststore``.

- The Python package directory in the Django project is referred to
  as ``./pyreststore/pyreststore``.


Prepare an isolated Python instance using virtualenv
----------------------------------------------------

One common problem with installing packages directly to your 
current site-packages area is that, 
you both often have more than one project 
and often use Python on your machine for things other than Django. 
In either of these cases, you may run into dependency issues between your 
applications and the installed packages. 
For this reason, I am using `virtualenv`_ to manage 
an isolated Python installation, containing a local Django installation. 
This is common, and recommended, practice among Python and Django users.

.. _`virtualenv`: https://virtualenv.pypa.io/

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
-----------------

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


Install the Python package requirements
---------------------------------------

The python package requirements are documented in ``./requirements.txt``.
To install the required Python packages using `pip`_, simply run::

  (pyreststoreEnv)$ pip install -r requirements.txt

This will also give You the Django installation described above.

.. _`pip`: https://pip.pypa.io/

You can verify Your Python version by running::

  $ python --version
  Python 2.7.6

You can verify Your Django version by running::

  $ python -c "import django; print(django.get_version())"
  1.8.3


Customize the settings
----------------------

Edit the file ``./pyreststore/pyreststore/settings.py``
to reflect Your needs.

Do **not** use the supplied version in production !


Create the model
----------------

We then need to create the model, and the associated database.

The central object in pyreststore is ``bckt``,
this model is used to store the contents
of the buckets and the associated metadata. 
The ``Bckt`` class is defined in ``./pyreststore/bckt/models.py``.

Create an initial migration for our model, 
and synconise it to the database for the first time::

  (pyreststoreEnv)./pyreststore$ python manage.py makemigrations bckt
  (pyreststoreEnv)./pyreststore$ python manage.py migrate

This does a lot of housekeeping for us, and creates the database 
in ``./pyreststore/db.sqllite3`` if You use the supplied settings.


Create an admin user
--------------------

To be able to create users and data in the application, 
we need to create a user who can login 
to the amin site. Run the following command::

  (pyreststoreEnv)./pyreststore$ python manage.py createsuperuser
  Username (leave blank to use 'peterdv'): admin
  Email address: peterdv@vestergaard.it
  Password: 
  Password (again): 
  Superuser created successfully.

and answer the prompts with Your desired values.


Start pyreststore
-----------------

Start the pyreststore web application::

  (pyreststoreEnv)./pyreststore$ python manage.py runserver



.. EOF
