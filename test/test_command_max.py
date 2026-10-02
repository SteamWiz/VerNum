from tempfile import NamedTemporaryFile
from wizlib.test_case import WizLibTestCase
from unittest.mock import Mock
from unittest.mock import patch
from io import StringIO

from wizlib.stream_handler import StreamHandler
from wizlib.config_handler import ConfigHandler

from vernum.command.max_command import MaxCommand
from vernum.command import VerNumCommand
from vernum import VerNumApp


class TestCommandMax(WizLibTestCase):

    def test_max(self):
        tx = "v1.2.3\nv1.0.6"
        a = VerNumApp()
        with \
                self.patchout() as o, self.patcherr() as e, \
                self.patch_stream(tx):
            a.parse_run('max')
            o.seek(0)
            n = o.read()
            self.assertEqual(n, '1.2.3')

    def test_no_input(self):
        tx = ""
        a = VerNumApp()
        with \
                self.patchout() as o, self.patcherr() as e, \
                self.patch_stream(tx):
            a.parse_run('max')
            o.seek(0)
            n = o.read()
            self.assertEqual(n, '')

    def test_max_patch_hyphen_scheme(self):
        tx = "v1.2.3\nv1.2.3-beta"
        a = VerNumApp(config={'vernum': {'scheme': 'patch-hyphen-al-be'}})
        with \
                self.patchout() as o, self.patcherr() as e, \
                self.patch_stream(tx):
            a.parse_run('max')
            o.seek(0)
            n = o.read()
            self.assertEqual(n, '1.2.3')
