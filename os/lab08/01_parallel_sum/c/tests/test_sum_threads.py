import unittest
import subprocess
import re
import os

class TestSumC(unittest.TestCase):
    def setUp(self):
        self.bin = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sum_threads'))

    def test_correct_sum(self):
        result = subprocess.run(
            [self.bin],
            input="20\n",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=5
        )
        self.assertEqual(result.returncode, 0)
        out = result.stdout
        array_line = next(line for line in out.splitlines() if line.startswith("Array:"))
        numbers = list(map(int, re.findall(r'\d+', array_line)))
        expected = sum(numbers)
        reported = int(re.search(r"Total sum:\s*(\d+)", out).group(1))
        self.assertEqual(expected, reported)
