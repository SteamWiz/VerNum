from wizlib.test_case import WizLibTestCase
from vernum.scheme import Scheme
from vernum.scheme.minor_scheme import MinorScheme


class TestMinorScheme(WizLibTestCase):

    def test_load(self):
        s = Scheme.family_member('name', 'minor')
        v = s.parse('v3.4')
        self.assertEqual(str(v), '3.4')

    def test_major(self):
        v = MinorScheme.parse('v3.4')
        n = v.increment('major')
        self.assertEqual(str(n), '4.0')

    def test_minor(self):
        v = MinorScheme.parse('v3.4')
        n = v.increment('minor')
        self.assertEqual(str(n), '3.5')
