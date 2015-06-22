#  -*- coding: utf-8 -*-
import django_generate_secretkey

try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup


setup(
    name='django-generate-secretkey',
    version=django_generate_secretkey.__version__,
    description=('Generates Django SECRET_KEY with management '
                 'command and adds to settings.'),
    long_description=open('README.rst').read(),
    license='GPLv2',
    author='Michal Klich',
    author_email='michal@michalklich.com',
    include_package_data=True,
    packages=['django_generate_secretkey'],
    url='https://github.com/inirudebwoy/django-generate-secretkey',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License v2',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
