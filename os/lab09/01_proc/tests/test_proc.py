import unittest
import subprocess
import os
import re
import time
import signal

class TestProc(unittest.TestCase):
    def setUp(self):
        self.binary = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'proc'))

    def test_proc_prints_pid_and_counter(self):
        proc = subprocess.Popen(
            [self.binary, "1"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        time.sleep(3)
        proc.send_signal(signal.SIGTERM)

        try:
            out, err = proc.communicate(timeout=2)
        except subprocess.TimeoutExpired:
            proc.kill()
            out, err = proc.communicate()

        lines = out.strip().splitlines()
        self.assertGreaterEqual(len(lines), 2)

        for line in lines:
            self.assertRegex(line, r'^\d+: \d+$')

        counters = [int(line.split(":")[1]) for line in lines]
        self.assertEqual(counters, list(range(len(counters))))

if __name__ == '__main__':
    unittest.main()