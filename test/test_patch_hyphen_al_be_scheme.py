from wizlib.test_case import WizLibTestCase
from unittest import skip

from vernum.command.max_command import MaxCommand
from vernum.scheme import Scheme
from vernum.scheme.patch_hyphen_al_be_scheme import PatchHyphenAlBeScheme


class TestPatchHyphenAlBeScheme(WizLibTestCase):

    def test_in_out(self):
        v = PatchHyphenAlBeScheme.parse('v3.4.2-alpha')
        self.assertEqual(str(v), '3.4.2-alpha')

    def test_no_pre(self):
        v = PatchHyphenAlBeScheme.parse('3.4.2')
        self.assertEqual(str(v), '3.4.2')

    def test_load(self):
        s = Scheme.family_member('name', 'patch-hyphen-al-be')
        v = s.parse('3.4.2-beta')
        self.assertEqual(str(v), '3.4.2-beta')

    def test_alpha_nothing(self):
        v = PatchHyphenAlBeScheme.parse('v3.4.2')
        n = v.increment('alpha')
        self.assertEqual(None, n)

    def test_beta_from_alpha(self):
        v = PatchHyphenAlBeScheme.parse('v3.4.2-alpha')
        n = v.increment('beta')
        self.assertEqual(str(n), '3.4.2-beta')

    def test_major(self):
        v = PatchHyphenAlBeScheme.parse('v3.4.2-alpha')
        n = v.increment('major')
        self.assertEqual(str(n), '4.0.0-alpha')

    def test_major_no_pre(self):
        v = PatchHyphenAlBeScheme.parse('v3.4.2')
        n = v.increment('major')
        self.assertEqual(str(n), '4.0.0-alpha')

    def test_major_zero(self):
        v = PatchHyphenAlBeScheme.parse('v3.4.2-alpha')
        n = v.increment('major-zero')
        self.assertEqual(str(n), '4.0.0')

    def test_major_zero_from_albe(self):
        v = PatchHyphenAlBeScheme.parse('v3.0.0-alpha')
        n = v.increment('major-zero')
        self.assertEqual(str(n), '3.0.0')

    def test_major_zero_no_pre(self):
        v = PatchHyphenAlBeScheme.parse('v3.4.2')
        n = v.increment('major-zero')
        self.assertEqual(str(n), '4.0.0')

    def test_minor(self):
        v = PatchHyphenAlBeScheme.parse('v3.4.2-alpha')
        n = v.increment('minor')
        self.assertEqual(str(n), '3.5.0-alpha')

    def test_minor_zero(self):
        v = PatchHyphenAlBeScheme.parse('v3.4.2-beta')
        n = v.increment('minor-zero')
        self.assertEqual(str(n), '3.5.0')

    def test_major_from_beta(self):
        v = PatchHyphenAlBeScheme.parse('v3.4.2-beta')
        n = v.increment('major')
        self.assertEqual(str(n), '4.0.0-alpha')

    def test_major_zero_from_beta(self):
        v = PatchHyphenAlBeScheme.parse('v3.4.2-beta')
        n = v.increment('major-zero')
        self.assertEqual(str(n), '4.0.0')

    def test_minor_from_no_pre(self):
        v = PatchHyphenAlBeScheme.parse('v3.4.2')
        n = v.increment('minor')
        self.assertEqual(str(n), '3.5.0-alpha')

    def test_minor_zero_from_no_pre(self):
        v = PatchHyphenAlBeScheme.parse('v3.4.2')
        n = v.increment('minor-zero')
        self.assertEqual(str(n), '3.5.0')

    def test_alpha_from_beta(self):
        v = PatchHyphenAlBeScheme.parse('v3.4.2-beta')
        n = v.increment('alpha')
        self.assertEqual(None, n)

    def test_patch_from_alpha(self):
        v = PatchHyphenAlBeScheme.parse('v3.4.2-alpha')
        n = v.increment('patch')
        self.assertEqual(str(n), '3.4.3-alpha')

    def test_patch_zero_from_alpha(self):
        v = PatchHyphenAlBeScheme.parse('v3.4.2-alpha')
        n = v.increment('patch-zero')
        self.assertEqual(str(n), '3.4.2')

    def test_patch_from_beta(self):
        v = PatchHyphenAlBeScheme.parse('v3.4.2-beta')
        n = v.increment('patch')
        self.assertEqual(str(n), '3.4.3-alpha')

    def test_patch_zero_from_beta(self):
        v = PatchHyphenAlBeScheme.parse('v3.4.2-beta')
        n = v.increment('patch-zero')
        self.assertEqual(str(n), '3.4.2')

    def test_patch_from_no_pre(self):
        v = PatchHyphenAlBeScheme.parse('v3.4.2')
        n = v.increment('patch')
        self.assertEqual(str(n), '3.4.3-alpha')

    def test_patch_zero_from_no_pre(self):
        v = PatchHyphenAlBeScheme.parse('v3.4.2')
        n = v.increment('patch-zero')
        self.assertEqual(str(n), '3.4.3')
