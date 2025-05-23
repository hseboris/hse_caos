import unittest
import subprocess
import os
import time
import signal

class TestCatchSig(unittest.TestCase):
    def setUp(self):
        self.binary = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'catchsig'))

    def test_catches_sigint(self):
        proc = subprocess.Popen(
            [self.binary, "1", "INT"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        time.sleep(1.5)
        os.kill(proc.pid, signal.SIGINT)
        time.sleep(1)
        proc.terminate()
        out, _ = proc.communicate()

        self.assertIn("[Caught: Interrupt]", out)

    def test_catches_abrt(self):
        proc = subprocess.Popen(
            [self.binary, "1", "ABRT"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        time.sleep(1.5)
        os.kill(proc.pid, signal.SIGABRT)
        time.sleep(1)
        proc.terminate()
        out, _ = proc.communicate()

        self.assertIn("[Caught: Aborted]", out)

if __name__ == '__main__':
    unittest.main()
