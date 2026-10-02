from wizlib.test_case import WizLibTestCase
from vernum.scheme.patch_scheme import PatchScheme


class TestPatchScheme(WizLibTestCase):

    def test_major(self):
        v = PatchScheme.parse('v3.4.5')
        n = v.increment('major')
        self.assertEqual(str(n), '4.0.0')

    def test_minor(self):
        v = PatchScheme.parse('v3.4.5')
        n = v.increment('minor')
        self.assertEqual(str(n), '3.5.0')

    def test_patch(self):
        v = PatchScheme.parse('v3.4.5')
        n = v.increment('patch')
        self.assertEqual(str(n), '3.4.6')
