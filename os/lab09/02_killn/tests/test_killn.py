import unittest
import subprocess
import os
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

    def test_kill_sleep_process(self):
        proc = subprocess.Popen(["sleep", "5"])
        time.sleep(0.5)

        result = subprocess.run(
            [self.binary, str(proc.pid), "TERM"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        proc.wait(timeout=3)

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
        self.assertIn("Failed to send signal", result.stderr)

if __name__ == '__main__':
    unittest.main()