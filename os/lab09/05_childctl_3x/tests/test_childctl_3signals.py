import unittest
import subprocess
import os
import signal
import time

class TestChildCtl3x(unittest.TestCase):
    def setUp(self):
        self.binary = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'childctl_3x'))

    def test_three_signals_to_exit(self):
        proc = subprocess.Popen(
            [self.binary, "1", "INT", "INT", "QUIT"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        time.sleep(2)
        for _ in range(3):
            os.kill(proc.pid, signal.SIGINT)
            time.sleep(1)

        out, err = proc.communicate(timeout=3)

        self.assertIn("Parent heartbeat", out)
        self.assertEqual(out.count("[Caught: Interrupt]"), 3)
        self.assertIn("Exiting after 3 INT signals", out)
        self.assertEqual(proc.returncode, 0)

if __name__ == '__main__':
    unittest.main()