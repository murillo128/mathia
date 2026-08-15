import unittest
from math import gcd

from experiments.pre_rl_signal.math_world import (
    affine_is_permutation,
    cancellation_counterexample,
    cancellation_is_valid,
    crt_collision,
    crt_map_is_bijection,
    functional_graph_all_vertices_on_cycles,
    gcd_reduction_preserves,
    linear_congruence_solutions,
    multiplication_is_permutation,
)


class MathWorldTests(unittest.TestCase):
    def test_multiplication_permutation_iff_coprime(self):
        for n in range(2, 40):
            for a in range(n):
                self.assertEqual(multiplication_is_permutation(a, n), gcd(a, n) == 1)

    def test_cancellation_iff_coprime(self):
        for n in range(2, 40):
            for a in range(n):
                self.assertEqual(cancellation_is_valid(a, n), gcd(a, n) == 1)

    def test_affine_permutation_depends_only_on_multiplier(self):
        for n in range(2, 24):
            for a in range(n):
                expected = gcd(a, n) == 1
                for b in (0, 1, n - 1):
                    self.assertEqual(affine_is_permutation(a, b, n), expected)

    def test_linear_congruence_solution_count(self):
        for n in range(2, 32):
            for a in range(n):
                d = gcd(a, n)
                for b in range(n):
                    count = len(linear_congruence_solutions(a, b, n))
                    expected = d if b % d == 0 else 0
                    self.assertEqual(count, expected)

    def test_reversible_finite_map_has_only_cycles(self):
        for n in range(2, 30):
            for a in range(n):
                self.assertEqual(
                    functional_graph_all_vertices_on_cycles(a, n),
                    gcd(a, n) == 1,
                )

    def test_gcd_reduction_is_invariant(self):
        for a in range(-20, 21):
            for b in range(-12, 13):
                for q in range(-4, 5):
                    self.assertTrue(gcd_reduction_preserves(a, b, q))

    def test_crt_map_bijection_iff_coprime(self):
        for m in range(2, 12):
            for n in range(2, 12):
                self.assertEqual(crt_map_is_bijection(m, n), gcd(m, n) == 1)

    def test_counterexample_witnesses_are_real(self):
        for n in range(2, 24):
            for a in range(n):
                witness = cancellation_counterexample(a, n)
                if gcd(a, n) == 1:
                    self.assertIsNone(witness)
                else:
                    self.assertIsNotNone(witness)
                    x, y = witness
                    self.assertNotEqual(x % n, y % n)
                    self.assertEqual((a * x - a * y) % n, 0)

    def test_crt_collision_exists_exactly_when_not_coprime(self):
        for m in range(2, 10):
            for n in range(2, 10):
                witness = crt_collision(m, n)
                if gcd(m, n) == 1:
                    self.assertIsNone(witness)
                else:
                    self.assertIsNotNone(witness)
                    x, y = witness
                    self.assertNotEqual(x % (m * n), y % (m * n))
                    self.assertEqual(x % m, y % m)
                    self.assertEqual(x % n, y % n)


if __name__ == "__main__":
    unittest.main()
