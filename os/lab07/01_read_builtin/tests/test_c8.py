import unittest
import subprocess
import os

class TestC8ReadBuiltin(unittest.TestCase):
    def setUp(self):
        self.script = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'c8.sh'))
        os.chmod(self.script, 0o755)

    def test_with_name(self):
        result = subprocess.run(
            [self.script],
            input="Spot\n",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        output = result.stdout.strip().splitlines()
        self.assertEqual(output[0], "Enter your name: Spot")
        self.assertEqual(output[1], "Hello, Spot!")

    def test_empty_input(self):
        result = subprocess.run(
            [self.script],
            input="\n",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        output = result.stdout.strip().splitlines()
        self.assertEqual(output[0], "Enter your name:")
        self.assertEqual(output[1], "Hello, tmpuser?")

if __name__ == '__main__':
    unittest.main()
