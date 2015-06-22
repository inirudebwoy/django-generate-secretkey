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

    def handle(self, *args, **options):
        # Create a random SECRET_KEY to put it in the main settings.
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        rnd_str = get_random_string(50, chars)
        if options['print']:
            self.stdout.write(rnd_str)
        elif options['show']:
            self.stdout.write("SECRET_KEY='%s'" % rnd_str)
        else:
            self.stdout.write('saving')
