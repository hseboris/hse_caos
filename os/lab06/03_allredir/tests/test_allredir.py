import unittest
import subprocess
import os

class TestAllRedir(unittest.TestCase):
    def setUp(self):
        self.bin = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'allredir'))
        self.input_file = 'test_input.txt'
        self.output_file = 'test_output.txt'
        with open(self.input_file, 'w') as f:
            f.write('hello 123\nline 2\n')

    def tearDown(self):
        for f in [self.input_file, self.output_file]:
            if os.path.exists(f):
                os.remove(f)

    def test_cat(self):
        result = subprocess.run([self.bin, 'cat', self.input_file, self.output_file],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True,
                                timeout=5)
        self.assertEqual(result.returncode, 0)
        self.assertIn('received 0', result.stdout.strip())
        with open(self.input_file) as fin, open(self.output_file) as fout:
            self.assertEqual(fin.read(), fout.read())

    def test_wc(self):
        result = subprocess.run([self.bin, 'wc', self.input_file, self.output_file],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True,
                                timeout=5)
        self.assertEqual(result.returncode, 0)
        self.assertIn('received 0', result.stdout.strip())
        with open(self.output_file) as f:
            self.assertIn("2", f.read())  # 2 строки

if __name__ == '__main__':
    unittest.main()
