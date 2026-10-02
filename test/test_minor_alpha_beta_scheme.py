from wizlib.test_case import WizLibTestCase
from unittest import skip

from vernum.command.max_command import MaxCommand
from vernum.scheme import Scheme
from vernum.scheme.minor_alpha_beta_scheme import MinorAlphaBetaScheme


# @skip
class TestMinorAlphaBetaScheme(WizLibTestCase):

    def test_in_out(self):
        v = MinorAlphaBetaScheme.parse('v3.4.alpha2')
        self.assertEqual(str(v), '3.4.alpha2')

    def test_load(self):
        s = Scheme.family_member('name', 'minor-alpha-beta')
        v = s.parse('3.4.alpha2')
        self.assertEqual(str(v), '3.4.alpha2')

    def test_alpha_simple(self):
        v = MinorAlphaBetaScheme.parse('v3.4.alpha2')
        n = v.increment('alpha')
        self.assertEqual(str(n), '3.4.alpha3')

    def test_beta_simple(self):
        v = MinorAlphaBetaScheme.parse('v3.4.beta2')
        n = v.increment('beta')
        self.assertEqual(str(n), '3.4.beta3')

    def test_beta_from_alpha(self):
        v = MinorAlphaBetaScheme.parse('v3.4.alpha2')
        n = v.increment('beta')
        self.assertEqual(str(n), '3.4.beta1')

    def test_patch_simple(self):
        v = MinorAlphaBetaScheme.parse('v3.4.5')
        n = v.increment('patch')
        self.assertEqual(str(n), '3.4.6')

    def test_patch_from_beta(self):
        v = MinorAlphaBetaScheme.parse('v3.4.beta2')
        n = v.increment('patch')
        self.assertEqual(str(n), '3.4.0')

    def test_patch_from_alpha(self):
        v = MinorAlphaBetaScheme.parse('v3.4.alpha2')
        n = v.increment('patch')
        self.assertEqual(str(n), '3.4.0')

    def test_minor_from_patch(self):
        v = MinorAlphaBetaScheme.parse('v3.4.5')
        n = v.increment('minor')
        self.assertEqual(str(n), '3.5.alpha1')

    def test_minor_from_beta(self):
        v = MinorAlphaBetaScheme.parse('v3.4.beta2')
        n = v.increment('minor')
        self.assertEqual(str(n), '3.5.alpha1')

    def test_minor_from_alpha(self):
        v = MinorAlphaBetaScheme.parse('v3.4.alpha2')
        n = v.increment('minor')
        self.assertEqual(str(n), '3.5.alpha1')

    def test_major(self):
        v = MinorAlphaBetaScheme.parse('v3.4.beta2')
        n = v.increment('major')
        self.assertEqual(str(n), '4.0.alpha1')

    def test_minor_zero(self):
        v = MinorAlphaBetaScheme.parse('v3.4.alpha2')
        n = v.increment('minor-zero')
        self.assertEqual(str(n), '3.5.0')

    def test_major_zero(self):
        v = MinorAlphaBetaScheme.parse('v3.4.alpha2')
        n = v.increment('major-zero')
        self.assertEqual(str(n), '4.0.0')

    def test_alpha_from_beta(self):
        v = MinorAlphaBetaScheme.parse('v3.4.beta2')
        n = v.increment('alpha')
        self.assertEqual(str(n), '3.4.beta3')

    def test_alpha_from_patch(self):
        v = MinorAlphaBetaScheme.parse('v3.4.5')
        n = v.increment('alpha')
        self.assertIsNone(n)

        # Left off here!

    # def test_scheme_config_in_python(self):
    #         tx = "v1.2.3\nv1.0.6\nv1.3.alpha1"
    #         c = MaxCommand(input=tx, vernum_scheme='alpha-beta')
    #         n = c.execute()
    #         self.assertEqual(n, '1.3.alpha1')
