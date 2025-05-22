import unittest
import subprocess
import os

class TestKilln(unittest.TestCase):
    def setUp(self):
        self.binary = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'killn'))

    def test_no_such_signal(self):
        result = subprocess.run(
            [self.binary, "1234", "FAKESIGNAL"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        self.assertIn("No such signal", result.stderr)
        self.assertEqual(result.returncode, 1)

    def test_invalid_pid_zero(self):
        result = subprocess.run(
            [self.binary, "0", "TERM"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        self.assertIn("Invalid PID", result.stderr)
        self.assertEqual(result.returncode, 1)

    def test_missing_arguments(self):
        result = subprocess.run(
            [self.binary],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Usage:", result.stderr)

if __name__ == '__main__':
    unittest.main()