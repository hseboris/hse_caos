import unittest
import subprocess
import os
import re

class TestProc(unittest.TestCase):
    def setUp(self):
        self.bin = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'proc'))

    def test_proc_prints_pid_and_counter(self):
        result = subprocess.run(
            ['timeout', '5', self.bin, '2'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=10
        )
        output = result.stdout.strip().splitlines()
        self.assertGreaterEqual(len(output), 2)
        for line in output:
            self.assertRegex(line, r'^\d+: \d+$')
        counters = [int(line.split(":")[1]) for line in output]
        self.assertEqual(counters, list(range(len(counters))))

if __name__ == '__main__':
    unittest.main()
