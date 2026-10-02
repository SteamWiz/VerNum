from argparse import ArgumentError
from wizlib.test_case import WizLibTestCase
from unittest.mock import Mock
from unittest.mock import patch
from io import StringIO
from tempfile import NamedTemporaryFile

from wizlib.stream_handler import StreamHandler

from vernum.command.next_command import NextCommand
from vernum.command import VerNumCommand
from vernum import VerNumApp
from vernum.error import VerNumError


class TestCommandNext(WizLibTestCase):

    def test_next_nothing(self):
        a = VerNumApp()
        with \
                self.patchout() as o, self.patcherr() as e, \
                self.assertRaises(ArgumentError), \
                self.patch_stream('v1.2.3'):
            a.parse_run('next')

    def test_major(self):
        tx = "v1.2.3"
        a = VerNumApp(config={'vernum': {'scheme': 'patch'}})
        with \
                self.patchout() as o, self.patcherr() as e, \
                self.patch_stream(tx):
            a.parse_run('next', 'major')
            o.seek(0)
            n = o.read()
            self.assertEqual(n, '2.0.0')

    def test_invalid_increment(self):
        a = VerNumApp()
        with \
                self.patchout() as o, self.patcherr() as e, \
                self.assertRaises(VerNumError), \
                self.patch_stream('v1.2.3'):
            a.parse_run('next', 'alpha')

    def test_invalid_input_string(self):
        a = VerNumApp()
        with \
                self.patchout() as o, self.patcherr() as e, \
                self.assertRaises(VerNumError), \
                self.patch_stream('v1.g.3'):
            a.parse_run('next', 'patch')
