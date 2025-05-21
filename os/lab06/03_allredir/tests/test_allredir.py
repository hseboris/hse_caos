import unittest
import subprocess
import os

class TestAllRedir(unittest.TestCase):
    def setUp(self):
        self.bin = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'allredir'))
        self.input_file = 'input_test.txt'
        self.output_file = 'dump_out.txt'
        with open(self.input_file, 'w') as f:
            f.write('test 123\nabc def\n')

    def tearDown(self):
        for f in [self.input_file, self.output_file]:
            if os.path.exists(f):
                os.remove(f)

    def test_hexdump(self):
        proc = subprocess.run([self.bin, 'hexdump', self.input_file, self.output_file],
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              text=True)
        self.assertEqual(proc.returncode, 0)
        self.assertTrue(proc.stdout.strip().startswith('received '))
        with open(self.output_file) as f:
            contents = f.read()
        self.assertIn("0000000", contents)  # проверим, что hexdump сработал

    def test_cat(self):
        proc = subprocess.run([self.bin, 'cat', self.input_file, self.output_file],
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              text=True)
        self.assertEqual(proc.returncode, 0)
        self.assertTrue(proc.stdout.strip(), "received 0")
        with open(self.output_file) as f:
            contents = f.read()
        with open(self.input_file) as f_in:
            expected = f_in.read()
        self.assertEqual(contents, expected)

if __name__ == '__main__':
    unittest.main()
