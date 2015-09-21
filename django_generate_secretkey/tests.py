from tempfile import mkstemp

from django.test import TestCase

from django_generate_secretkey.management.commands.generate_key import Command


def fill_file(file_path, text):
    with open(file_path, 'w') as file_:
        file_.write(text)


class CommandTestCase(TestCase):
    def setUp(self):
        self.command = Command()
        _, self.tmp_path = mkstemp()

    def test_replace_pattern_not_found(self):
        fill_file(self.tmp_path, 'bazinga')

        self.command._replace_line(self.tmp_path, 'not in file', 'foobar')
        for line in open(self.tmp_path):
            assert 'bazinga' in line
            assert not ('foobar' in line)

    def test_replace_pattern_found_once(self):
        fill_file(self.tmp_path, 'foo')

        self.command._replace_line(self.tmp_path, 'foo', 'bar')
        for line in open(self.tmp_path):
            assert 'bar' in line
            assert not ('foo' in line)

    def test_replace_pattern_found_more_than_once(self):
        fill_file(self.tmp_path, 'foo\nwaat\nfoo\nsomething')

        self.command._replace_line(self.tmp_path, 'foo', 'bar')
        for line in open(self.tmp_path):
            assert not ('foo' in line)
