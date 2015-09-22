import re
from tempfile import mkstemp
from shutil import move
from os import remove, close, linesep

from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string


SECRET_KEY_SETTINGS = "SECRET_KEY = '%s'" + linesep
SECRET_KEY_PATTERN = r'^SECRET_KEY ?='


class Command(BaseCommand):
    help = 'Generate SECRET_KEY and save it in settings file'

    def add_arguments(self, parser):
        parser.add_argument('-p', '--print', action='store_true',
                            help=('Print key to stdout instead saving in '
                                  'settings file.'))
        parser.add_argument('path', nargs='?',
                            help='Save key in settings file, provide path')

    def handle(self, *args, **options):
        # Create a random SECRET_KEY to put it in the main settings.
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        rnd_str = get_random_string(50, chars)

        if options['print']:
            self._print_random_string(rnd_str)
        elif options['path']:
            self._replace_in_file(rnd_str, options['path'])
        else:
            self._print_django_key(rnd_str)

    def _replace_line(self, file_path, line_pattern, new_line):
        fh, temp_path = mkstemp()
        with open(temp_path, 'w') as new_file:
            with open(file_path) as old_file:
                for line in old_file:
                    secret_key = re.match(line_pattern, line)
                    if secret_key:
                        line = new_line
                    new_file.write(line)

        close(fh)
        remove(file_path)
        move(temp_path, file_path)

    def _print_random_string(self, rnd_str):
        self.stdout.write(rnd_str)

    def _print_django_key(self, rnd_str):
        self.stdout.write(SECRET_KEY_SETTINGS % rnd_str)

    def _replace_in_file(self, rnd_str, path):
        try:
            self._replace_line(path, SECRET_KEY_PATTERN,
                               SECRET_KEY_SETTINGS % rnd_str)
        except IOError:
            self.stdout.write('Could not replace the value in file.'
                              'Check if file {} exists.'.format(path))
