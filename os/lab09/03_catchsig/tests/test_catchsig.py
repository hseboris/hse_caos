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

    def test_catches_term(self):
        out = self.run_and_kill("TERM", signal.SIGTERM)
        self.assertRegex(out, r"\[Caught: .*Term.*\]")

    def test_catches_pipe(self):
        out = self.run_and_kill("PIPE", signal.SIGPIPE)
        self.assertRegex(out, r"\[Caught: .*Pipe.*\]")

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
            [self.binary, "1", "INT", "TERM", "PIPE"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        time.sleep(2)
        os.kill(proc.pid, signal.SIGPIPE)
        time.sleep(2)
        os.kill(proc.pid, signal.SIGTERM)
        time.sleep(2)
        os.kill(proc.pid, signal.SIGINT)
        time.sleep(1)
        proc.terminate()
        out, _ = proc.communicate()

        self.assertRegex(out, r"\[Caught: .*Pipe.*\]")
        self.assertRegex(out, r"\[Caught: .*Term.*\]")
        self.assertRegex(out, r"\[Caught: .*Interrupt.*\]")

if __name__ == '__main__':
    unittest.main()
