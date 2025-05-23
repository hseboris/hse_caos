import unittest
import subprocess
import os
import signal
import time

class TestChildCtl(unittest.TestCase):
    def setUp(self):
        self.binary = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'childctl'))

    def test_heartbeat_and_quit(self):
        proc = subprocess.Popen(
            [self.binary, "1", "INT", "INT", "USR1"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        time.sleep(3)
        os.kill(proc.pid, signal.SIGINT)  # send quit signal
        time.sleep(2)

        out, err = proc.communicate(timeout=2)

        self.assertIn("Parent heartbeat", out)
        self.assertIn("Caught: Interrupt", out)
        self.assertIn("Quitting...", out)
        self.assertIn("Child terminated", out)
        self.assertEqual(proc.returncode, 0)

if __name__ == '__main__':
    unittest.main()
