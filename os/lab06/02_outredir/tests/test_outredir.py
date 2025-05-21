import unittest
import subprocess
import os

class TestOutRedir(unittest.TestCase):
    def setUp(self):
        self.bin = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'outredir'))

    def tearDown(self):
        for f in os.listdir():
            if f.startswith('out_of_'):
                try:
                    os.remove(f)
                except Exception:
                    pass

    def test_basic_ls(self):
        outfile = "out_of_ls"
        subprocess.run([self.bin, "ls", outfile], check=True)
        with open(outfile) as f:
            contents = f.read()
        self.assertTrue("outredir.c" in contents or "Makefile" in contents)

    def test_echo(self):
        outfile = "out_of_echo"
        subprocess.run([self.bin, "echo", "hello", outfile], check=True)
        with open(outfile) as f:
            contents = f.read().strip()
        self.assertEqual(contents, "hello")

    def test_invalid_command(self):
        outfile = "out_of_fail"
        result = subprocess.run([self.bin, "nosuchcmd", outfile],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True)
        self.assertNotEqual(result.returncode, 0)
        # файл не должен быть создан или должен быть пустым
        if os.path.exists(outfile):
            with open(outfile) as f:
                contents = f.read().strip()
            self.assertEqual(contents, "")

if __name__ == '__main__':
    unittest.main()
