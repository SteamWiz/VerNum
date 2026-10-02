from vernum import VerNumApp
from wizlib.test_case import WizLibTestCase

from wizlib.stream_handler import StreamHandler
from wizlib.config_handler import ConfigHandler

from vernum.command.limit_command import LimitCommand
from vernum.error import VerNumError


class TestLimitCommand(WizLibTestCase):

    def test_limit(self):
        tx = "v1.2.3"
        a = VerNumApp(config={'vernum': {'limit': {'min': 'v1.1.0'}}})
        with \
                self.patchout() as o, self.patcherr() as e, \
                self.patch_stream(tx):
            a.parse_run('limit')
            o.seek(0)
            n = e.read()
            self.assertIn(n, 'v1.2.3 >= v1.1.0')

    def test_limit_fail(self):
        tx = "v1.2.3"
        a = VerNumApp(config={'vernum': {'limit': {'min': 'v1.3.0'}}})
        with \
                self.patchout() as o, self.patcherr() as e, \
                self.assertRaises(VerNumError), \
                self.patch_stream(tx):
            a.parse_run('limit')

    def test_limit_invalid(self):
        tx = "v1.a"
        a = VerNumApp(config={'vernum': {'limit': {'min': 'v1.3.0'}}})
        with \
                self.patchout() as o, self.patcherr() as e, \
                self.assertRaises(VerNumError), \
                self.patch_stream(tx):
            a.parse_run('limit')
