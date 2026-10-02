from wizlib.test_case import WizLibTestCase
from vernum.scheme import Scheme
from vernum.scheme.major_scheme import MajorScheme


class TestMajorScheme(WizLibTestCase):

    def test_load(self):
        s = Scheme.family_member('name', 'major')
        v = s.parse('v3')
        self.assertEqual(str(v), '3')

    def test_major(self):
        v = MajorScheme.parse('v3')
        n = v.increment('major')
        self.assertEqual(str(n), '4')

    # def test_minor(self):
    #     v = MinorScheme.parse('v3.4')
    #     n = v.increment('minor')
    #     self.assertEqual(str(n), '3.5')
