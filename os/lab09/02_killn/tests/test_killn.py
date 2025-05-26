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

    def test_missing_arguments(self):
        result = subprocess.run(
            [self.binary],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Usage:", result.stderr)

    def test_kill_self_with_safe_signal(self):
        result = subprocess.run(
            [self.binary, str(os.getpid()), "CONT"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr.strip(), "")

    def test_kill_invalid_pid(self):
        result = subprocess.run(
            [self.binary, "999999", "TERM"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("kill", result.stderr)

    def test_kill_self_with_usr1(self):
        result = subprocess.run(
            [self.binary, str(os.getpid()), "USR1"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        self.assertEqual(result.returncode, 0)

if __name__ == '__main__':
    unittest.main()