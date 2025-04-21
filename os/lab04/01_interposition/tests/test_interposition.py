import os
import sys
import unittest
import subprocess

class TestInterposition(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Собираем программу и библиотеку
        root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        result = subprocess.run(['make'], cwd=root,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            print(result.stdout, file=sys.stderr)
            print(result.stderr, file=sys.stderr)
            raise RuntimeError('Make failed')

    def test_link_time_interposition(self):
        root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        prog = os.path.join(root, 'program')
        result = subprocess.run([prog],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        self.assertEqual(result.returncode, 0)
        lines = result.stdout.strip().splitlines()
        self.assertEqual(lines[0], "john (link‑wrap): fred is called with 42")
        self.assertEqual(lines[1], "bill: you passed Hello World!")

    def test_load_time_interposition(self):
        root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        prog = os.path.join(root, 'program')
        libsam = os.path.join(root, 'libsam.so')
        env = os.environ.copy()
        env['LD_PRELOAD'] = libsam
        result = subprocess.run([prog], env=env,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        self.assertEqual(result.returncode, 0)
        lines = result.stdout.strip().splitlines()
        self.assertEqual(lines[0], "john (link‑wrap): fred is called with 42")
        self.assertEqual(lines[1], "sam (LD_PRELOAD): bill is called with Hello World!")
        self.assertEqual(lines[2], "bill: you passed Hello World!")

if __name__ == '__main__':
    unittest.main()