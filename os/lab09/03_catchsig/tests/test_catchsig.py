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
        time.sleep(1.5)
        os.kill(proc.pid, sig)
        time.sleep(1)
        proc.terminate()
        out, err = proc.communicate(timeout=2)
        return out

    def test_catches_sigint(self):
        out = self.run_and_kill("INT", signal.SIGINT)
        self.assertRegex(out, r"\[Caught: .*Interrupt.*\]")

    def test_catches_abrt(self):
        out = self.run_and_kill("ABRT", signal.SIGABRT)
        self.assertRegex(out, r"\[Caught: .*Abort.*\]")

    def test_catches_usr1(self):
        out = self.run_and_kill("USR1", signal.SIGUSR1)
        self.assertRegex(out, r"\[Caught: .*User.*\]")

    def test_ignores_invalid_signal(self):
        # запускаем с неверным сигналом
        result = subprocess.run(
            [self.binary, "1", "FAKESIGNAL"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        self.assertIn("Cannot handle signal", result.stderr)

    def test_multiple_signals(self):
        proc = subprocess.Popen(
            [self.binary, "1", "INT", "ABRT", "USR1"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        time.sleep(1)
        os.kill(proc.pid, signal.SIGUSR1)
        time.sleep(1)
        os.kill(proc.pid, signal.SIGINT)
        time.sleep(1)
        os.kill(proc.pid, signal.SIGABRT)
        time.sleep(1)
        proc.terminate()
        out, _ = proc.communicate()
        self.assertRegex(out, r"\[Caught: .*Interrupt.*\]")
        self.assertRegex(out, r"\[Caught: .*Abort.*\]")
        self.assertRegex(out, r"\[Caught: .*User.*\]")

if __name__ == '__main__':
    unittest.main()
