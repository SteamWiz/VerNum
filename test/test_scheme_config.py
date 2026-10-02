from vernum import VerNumApp
from wizlib.test_case import WizLibTestCase

from wizlib.stream_handler import StreamHandler
from wizlib.config_handler import ConfigHandler
from vernum.error import VerNumError

from vernum.command.max_command import MaxCommand
from vernum.command.next_command import NextCommand
from unittest.mock import patch


class TestSchemeConfig(WizLibTestCase):

    def setUp(self):
        super().setUp()
        self.env_patch = patch.object(ConfigHandler, 'env', return_value=None)
        self.env_patch.start()

    def tearDown(self):
        self.env_patch.stop()
        super().tearDown()

    def test_max_patch_scheme(self):
        tx = "v1.2.3\nv1.0.6"
        a = VerNumApp(config={'vernum': {'scheme': 'patch'}})
        with \
                self.patchout() as o, self.patcherr() as e, \
                self.patch_stream(tx):
            a.parse_run('max')
            o.seek(0)
            n = o.read()
            self.assertEqual(n, '1.2.3')

    def test_max_minor_scheme(self):
        tx = "v1.2\nv1.0"
        a = VerNumApp(config={'vernum': {'scheme': 'minor'}})
        self.assertEqual(a.config.get('vernum-scheme'), 'minor')
        with \
                self.patchout() as o, self.patcherr() as e, \
                self.patch_stream(tx):
            a.parse_run('max')
            o.seek(0)
            n = o.read()
            self.assertEqual(n, '1.2')

    def test_next_minor_scheme(self):
        a = VerNumApp(config={'vernum': {'scheme': 'minor'}})
        with \
                self.patchout() as o, self.patcherr() as e, \
                self.patch_stream('4.6'):
            a.parse_run('next', 'minor')
            o.seek(0)
            n = o.read()
            self.assertEqual(n, '4.7')

    def test_invalid_scheme(self):
        a = VerNumApp(config={'vernum': {'scheme': 'blah'}})
        with \
                self.patchout() as o, self.patcherr() as e, \
                self.assertRaises(VerNumError), \
                self.patch_stream('4.6'):
            a.parse_run('max')
