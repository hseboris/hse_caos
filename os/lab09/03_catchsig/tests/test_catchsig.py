import unittest
import subprocess
import os
import time
import signal

class TestCatchSig(unittest.TestCase):
    def setUp(self):
        self.binary = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'catchsig'))

    def run_and_kill(self, signame, sig):
        proc = subprocess.Popen(
            [self.binary, "1", signame],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        time.sleep(2.0)
        os.kill(proc.pid, sig)
        time.sleep(2.0)
        proc.terminate()
        out, err = proc.communicate(timeout=2)
        return out

    def test_catches_sigint(self):
        out = self.run_and_kill("INT", signal.SIGINT)
        self.assertRegex(out, r"\[Caught: .*Interrupt.*\]")

    def test_catches_usr1(self):
        out = self.run_and_kill("USR1", signal.SIGUSR1)
        self.assertRegex(out, r"\[Caught: .*User.*\]")

    def test_catches_alrm(self):
        out = self.run_and_kill("ALRM", signal.SIGALRM)
        self.assertRegex(out, r"\[Caught: .*Alarm.*\]")

    def test_invalid_signal(self):
        result = subprocess.run(
            [self.binary, "1", "FAKESIGNAL"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=2
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("No such signal", result.stderr)

    def test_multiple_signals(self):
        proc = subprocess.Popen(
            [self.binary, "1", "INT", "USR1", "ALRM"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        time.sleep(2)
        os.kill(proc.pid, signal.SIGUSR1)
        time.sleep(2)
        os.kill(proc.pid, signal.SIGALRM)
        time.sleep(2)
        os.kill(proc.pid, signal.SIGINT)
        time.sleep(1)
        proc.terminate()
        out, _ = proc.communicate()

        self.assertRegex(out, r"\[Caught: .*User.*\]")
        self.assertRegex(out, r"\[Caught: .*Interrupt.*\]")
        self.assertRegex(out, r"\[Caught: .*Alarm.*\]")

if __name__ == '__main__':
    unittest.main()
