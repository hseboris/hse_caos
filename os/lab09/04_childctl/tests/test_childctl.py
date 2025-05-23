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
            [self.binary, "1", "INT", "INT", "QUIT"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        time.sleep(2.5)
        os.kill(proc.pid, signal.SIGQUIT)
        time.sleep(0.5)
        os.kill(proc.pid, signal.SIGINT)
        out, err = proc.communicate(timeout=3)

        if not out.strip():
            print("STDERR:", err)

        self.assertIn("Parent heartbeat", out)
        self.assertRegex(out, r"\[Caught: Quit.*\]")
        self.assertRegex(out, r"\[Caught: Interrupt.*\]")
        self.assertIn("Exiting gracefully on signal INT", out)
        self.assertEqual(proc.returncode, 0)

if __name__ == '__main__':
    unittest.main()