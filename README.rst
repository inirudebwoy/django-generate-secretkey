=========================
django-generate-secretkey
=========================
.. image:: https://travis-ci.org/inirudebwoy/django-generate-secretkey.svg?branch=master
   :target: https://travis-ci.org/inirudebwoy/django-generate-secretkey

.. image:: https://readthedocs.org/projects/django-generate-secretkey/badge/?version=latest
   :target: https://readthedocs.org/projects/django-generate-secretkey/?badge=latest
   :alt: Documentation Status

Generates Django SECRET_KEY with management command and adds to settings.
Use within your automation scripts or deployment process.

Installation
============
Install from pip::

  pip install django-generate-secretkey

Add package to INSTALLED_APPS.::

  INSTALLED_APPS += ('django_generate_secretkey',)

Usage
=====

Examples are best.
Print full line to stdout::

  $ python manage.py generate_key
  SECRET_KEY = 'tdb=$j=1u$#813$6vg3r$jq_d(z^w3^3lnjrkjw9(k$#r0(a+4'

Print only generated key to stdout::

  $ python manage.py generate_key -p
  tdb=$j=1u$#813$6vg3r$jq_d(z^w3^3lnjrkjw9(k$#r0(a+4

Save in settings file, this will replace your existing key in file on provided path::

  $ python manage.py generate_key path/to/settings.py
