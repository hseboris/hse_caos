import unittest
import subprocess
import os

class TestPipeRedir(unittest.TestCase):
    def setUp(self):
        self.bin = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'piperedir'))

    def test_date_to_hexdump(self):
        result = subprocess.run(
            [self.bin, 'date', 'hexdump', '-C'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=5
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("00000000", result.stdout)
        self.assertRegex(result.stdout, r'\d{4}')

    def test_echo_to_wc(self):
        result = subprocess.run(
            [self.bin, 'echo', 'wc'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=5
        )
        self.assertEqual(result.returncode, 0)
        self.assertRegex(result.stdout.strip(), r'\b1\b')

if __name__ == '__main__':
    unittest.main()
