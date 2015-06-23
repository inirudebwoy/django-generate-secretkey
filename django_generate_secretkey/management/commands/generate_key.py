import re
from tempfile import mkstemp
from shutil import move
from os import remove, close
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = 'Generate SECRET_KEY and save it in settings file'

    def add_arguments(self, parser):
        # TODO: verify if these flags are available
        parser.add_argument('-p', '--print', action='store_true',
                            help=('Print key to stdout instead saving in '
                                  'settings file.'))
        parser.add_argument('-s', '--show', action='store_true')
        parser.add_argument('--path', help='Path to settings file, so simple')

    def handle(self, *args, **options):
        # Create a random SECRET_KEY to put it in the main settings.
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        rnd_str = get_random_string(50, chars)

        # TODO: kill these elif's
        if options['print']:
            self.stdout.write(rnd_str)
        elif options['show']:
            self.stdout.write("SECRET_KEY='%s'" % rnd_str)
        elif options['path']:
            self._replace(options['path'], r'^SECRET_KEY ?=',
                          "SECRET_KEY='%s'" % rnd_str)
            self.stdout.write('saving')

    def _replace(file_path, pattern, subst):
        fh, abs_path = mkstemp()
        with open(abs_path, 'w') as new_file:
            with open(file_path) as old_file:
                for line in old_file:
                    secret_key = re.match(r'^SECRET_KEY ?=', line)
                    if secret_key:
                        line = subst
                    new_file.write(line)

        close(fh)
        remove(file_path)
        move(abs_path, file_path)
