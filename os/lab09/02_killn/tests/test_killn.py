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
        self.assertIn("No such signal", result.stdout)
        self.assertEqual(result.returncode, 1)

    def test_invalid_pid(self):
        result = subprocess.run(
            [self.binary, "0", "TERM"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        self.assertIn("Invalid PID", result.stderr)
        self.assertEqual(result.returncode, 1)

    def test_kill_self(self):
        result = subprocess.run(
            [self.binary, str(os.getpid()), "USR1"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        # программа вернёт 0 (сигнал доставлен), даже если он не обрабатывается
        self.assertEqual(result.returncode, 0)

if __name__ == '__main__':
    unittest.main()
