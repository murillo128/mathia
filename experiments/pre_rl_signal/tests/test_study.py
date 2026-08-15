import unittest

from experiments.pre_rl_signal.study import (
    generate_hidden_tasks,
    generate_visible_situation,
    score_answer,
)


class StudyTests(unittest.TestCase):
    def test_visible_generation_is_deterministic(self):
        a = generate_visible_situation("reversibility", 11)
        b = generate_visible_situation("reversibility", 11)
        self.assertEqual(a, b)

    def test_hidden_generation_is_deterministic(self):
        a = generate_hidden_tasks("reversibility", 97, 10)
        b = generate_hidden_tasks("reversibility", 97, 10)
        self.assertEqual(a, b)

    def test_public_task_hides_ground_truth(self):
        task = generate_hidden_tasks("reversibility", 97, 1)[0]
        public = task.public_view()
        self.assertNotIn("ground_truth", public)
        self.assertIn("ground_truth", task.private_view())

    def test_visible_seed_does_not_control_hidden_seed(self):
        visible_a = generate_visible_situation("reversibility", 1)
        visible_b = generate_visible_situation("reversibility", 2)
        hidden_a = generate_hidden_tasks("reversibility", 999, 4)
        hidden_b = generate_hidden_tasks("reversibility", 999, 4)
        self.assertNotEqual(visible_a, visible_b)
        self.assertEqual(hidden_a, hidden_b)

    def test_scalar_scoring(self):
        tasks = generate_hidden_tasks("reversibility", 97, 5)
        for task in tasks:
            if task.answer_kind in {"bool", "int"}:
                self.assertTrue(score_answer(task, task.ground_truth))

    def test_collision_witness_scoring(self):
        tasks = generate_hidden_tasks("reversibility", 97, 12)
        witness_task = next(t for t in tasks if t.answer_kind == "collision_pair")
        a = witness_task.ground_truth["a"]
        n = witness_task.ground_truth["n"]
        witness = None
        for x in range(n):
            for y in range(x + 1, n):
                if (a * x - a * y) % n == 0:
                    witness = [x, y]
                    break
            if witness:
                break
        self.assertIsNotNone(witness)
        self.assertTrue(score_answer(witness_task, witness))
        self.assertFalse(score_answer(witness_task, [0, 0]))

    def test_crt_collision_witness_scoring(self):
        tasks = generate_hidden_tasks("decomposition", 97, 6)
        witness_task = next(t for t in tasks if t.answer_kind == "crt_collision_pair")
        m = witness_task.ground_truth["m"]
        n = witness_task.ground_truth["n"]
        modulus = m * n
        witness = None
        for x in range(modulus):
            for y in range(x + 1, modulus):
                if x % m == y % m and x % n == y % n:
                    witness = [x, y]
                    break
            if witness:
                break
        self.assertIsNotNone(witness)
        self.assertTrue(score_answer(witness_task, witness))


if __name__ == "__main__":
    unittest.main()
