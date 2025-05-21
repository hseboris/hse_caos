import unittest
import subprocess
import os

class TestFork(unittest.TestCase):
    def test_process_output_unordered(self):
        prog = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'fork'))
        p = subprocess.Popen([prog],
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             text=True)
        out, err = p.communicate()
        lines = out.strip().splitlines()
        self.assertEqual(p.returncode, 0)
        self.assertEqual(len(lines), 3)

        expected = {"Hello from Parent", "Hello from Child1", "Hello from Child2"}
        self.assertEqual(set(lines), expected)

if __name__ == '__main__':
    unittest.main()
