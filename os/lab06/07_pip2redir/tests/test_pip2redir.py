import unittest
import subprocess
import os

class TestPip2Redir(unittest.TestCase):
    def setUp(self):
        self.bin = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pip2redir'))

    def test_pipe_echo_wc(self):
        result = subprocess.run(
            [self.bin, 'echo', 'wc'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=5
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("child", result.stdout)
        self.assertRegex(result.stdout, r"child \d+ exited with 0")
        self.assertEqual(result.stdout.count("child "), 2)

    def test_pipe_date_cat(self):
        result = subprocess.run(
            [self.bin, 'date', 'cat'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=5
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("child", result.stdout)
        self.assertEqual(result.stdout.count("child "), 2)

if __name__ == '__main__':
    unittest.main()
