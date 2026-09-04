import unittest

from deployforge import plan


class DeployForgeTests(unittest.TestCase):
    def test_plan_is_sorted(self):
        self.assertEqual(
            plan([
                {"name": "web", "image": "nginx", "replicas": 2},
                {"name": "api", "image": "python", "replicas": 1},
            ])[0]["name"],
            "api",
        )

    def test_invalid_replicas(self):
        with self.assertRaises(ValueError):
            plan([{"name": "api", "image": "python", "replicas": 0}])


if __name__ == "__main__":
    unittest.main()
