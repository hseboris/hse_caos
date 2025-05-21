import unittest
import subprocess
import os

class TestArgRedir(unittest.TestCase):
    def setUp(self):
        self.bin = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'argredir'))
        self.input_file = 'input_argredir.txt'
        self.output_file = 'output_argredir.txt'
        with open(self.input_file, 'w') as f:
            f.write('hello 123\nsecond line\n')

    def tearDown(self):
        for f in [self.input_file, self.output_file]:
            if os.path.exists(f):
                os.remove(f)

    def test_cat_with_args(self):
        result = subprocess.run([self.bin, self.input_file, self.output_file, 'cat'],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True,
                                timeout=5)
        self.assertEqual(result.returncode, 0)
        self.assertIn('received 0', result.stdout.strip())
        with open(self.input_file) as fin, open(self.output_file) as fout:
            self.assertEqual(fin.read(), fout.read())

    def test_hexdump_with_args(self):
        result = subprocess.run([
            self.bin, self.input_file, self.output_file, 'hexdump', '-C'
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
        self.assertEqual(result.returncode, 0)
        self.assertIn('received 0', result.stdout.strip())
        with open(self.output_file) as f:
            self.assertIn('00000000', f.read())