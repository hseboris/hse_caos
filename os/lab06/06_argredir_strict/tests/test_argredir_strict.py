import unittest
import subprocess
import os

class TestArgRedirStrict(unittest.TestCase):
    def setUp(self):
        self.bin = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'argredir'))
        self.input_file = 'input_strict.txt'
        self.output_file = 'output_strict.txt'
        with open(self.input_file, 'w') as f:
            f.write('testing error check\n')

    def tearDown(self):
        for f in [self.input_file, self.output_file]:
            if os.path.exists(f):
                os.remove(f)

    def test_cat_success(self):
        result = subprocess.run(
            [self.bin, self.input_file, self.output_file, 'cat'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=5
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("received 0", result.stdout.strip())
        with open(self.output_file) as fout, open(self.input_file) as fin:
            self.assertEqual(fout.read(), fin.read())

    def test_bad_input_file(self):
        result = subprocess.run(
            [self.bin, "no_such_input", self.output_file, "cat"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=5
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("open input", result.stderr)

    def test_invalid_command(self):
        result = subprocess.run(
            [self.bin, self.input_file, self.output_file, "nosuchcommand"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=5
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("execvp", result.stderr)

if __name__ == '__main__':
    unittest.main()
