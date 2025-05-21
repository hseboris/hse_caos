import unittest
import subprocess
import os

class TestAllRedir(unittest.TestCase):
    def setUp(self):
        self.bin = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'allredir'))
        self.input_file = 'input_test.txt'
        self.output_file = 'output_test.txt'
        with open(self.input_file, 'w') as f:
            f.write('CAOS 2025\nhello world\n')

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
        self.assertIn("received 0", result.stdout.strip())

        with open(self.output_file) as f_out, open(self.input_file) as f_in:
            self.assertEqual(f_out.read(), f_in.read())

    def test_grep(self):
        result = subprocess.run([self.bin, 'grep', 'CAOS', self.input_file, self.output_file],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True,
                                timeout=5)
        self.assertEqual(result.returncode, 0)
        self.assertIn("received 0", result.stdout.strip())

        with open(self.output_file) as f:
            contents = f.read().strip()
        self.assertEqual(contents, "CAOS 2025")

if __name__ == '__main__':
    unittest.main()
