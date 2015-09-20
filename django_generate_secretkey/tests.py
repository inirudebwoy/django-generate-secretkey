from tempfile import mkstemp

from django.test import TestCase

from django_generate_secretkey.management.commands.generate_key import Command


class CommandTestCase(TestCase):
    def setUp(self):
        self.command = Command()
        _, self.tmp_path = mkstemp()

    def test_replace_pattern_not_found(self):
        self.command._replace(self.tmp_path, '', 'foobar')
        for line in open(self.tmp_path):
            assert('foobar' in line)

    def test_replace_pattern_found_once(self):
        with open(self.tmp_path, 'w') as tmp_file:
            tmp_file.write('foo')

        self.command._replace(self.tmp_path, 'foo', 'bar')
        for line in open(self.tmp_path):
            assert 'bar' in line
            assert not ('foo' in line)

    def test_replace_pattern_found_more_than_once(self):
        with open(self.tmp_path, 'w') as tmp_file:
            tmp_file.write('foo\nwaat\nfoo\nsomething')

        self.command._replace(self.tmp_path, 'foo', 'bar')
        for line in open(self.tmp_path):
            assert not ('foo' in line)
