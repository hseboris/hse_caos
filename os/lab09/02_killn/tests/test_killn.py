import unittest
import subprocess
import os
import signal
import time

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

    def test_signal_delivery_to_child(self):
        child = subprocess.Popen(['sleep', '10'])
        time.sleep(0.2)
        result = subprocess.run(
            [self.binary, str(child.pid), "TERM"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        child.wait(timeout=2)

        self.assertEqual(result.returncode, 0)
        self.assertEqual(child.returncode, -signal.SIGTERM)

if __name__ == '__main__':
    unittest.main()
