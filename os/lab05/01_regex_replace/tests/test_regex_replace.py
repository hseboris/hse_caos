import unittest
import subprocess
import random
import string

class TestRegexReplace(unittest.TestCase):
    def run_solution(self, pattern, text, replacement):
        process = subprocess.Popen(
            ['./solution', pattern, text, replacement],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        output, err = process.communicate()
        return process.returncode, output.strip(), err.strip()

    def test_simple_replace(self):
        rc, out, _ = self.run_solution('a', 'abcabc', 'x')
        self.assertEqual(rc, 0)
        self.assertEqual(out, 'xbcxbc')

    def test_no_match(self):
        rc, out, _ = self.run_solution('z', 'abcabc', 'x')
        self.assertEqual(rc, 0)
        self.assertEqual(out, 'abcabc')

    def test_full_replace(self):
        rc, out, _ = self.run_solution('abc', 'abcabc', 'x')
        self.assertEqual(rc, 0)
        self.assertEqual(out, 'xx')

    def test_empty_text(self):
        rc, out, _ = self.run_solution('a', '', 'x')
        self.assertEqual(rc, 0)
        self.assertEqual(out, '')

    def test_replace_digit(self):
        # POSIX syntax: [0-9]+ instead of \d+
        rc, out, _ = self.run_solution(r'[0-9]+', 'abc123def456', '_')
        self.assertEqual(rc, 0)
        self.assertEqual(out, 'abc_def_')

    def test_replace_start(self):
        rc, out, _ = self.run_solution('^abc', 'abc xyz abc', 'START')
        self.assertEqual(rc, 0)
        self.assertEqual(out, 'START xyz abc')

    def test_replace_end(self):
        rc, out, _ = self.run_solution('abc$', 'xyz abc', 'END')
        self.assertEqual(rc, 0)
        self.assertEqual(out, 'xyz END')

    def test_special_characters(self):
        rc, out, _ = self.run_solution(r'\.', 'a.b.c', 'DOT')
        self.assertEqual(rc, 0)
        self.assertEqual(out, 'aDOTbDOTc')

    def test_repeated_patterns(self):
        rc, out, _ = self.run_solution('aa', 'aaaaaa', 'x')
        self.assertEqual(rc, 0)
        self.assertEqual(out, 'xxx')

    def test_long_input(self):
        text = ''.join(random.choice('ab') for _ in range(10000))
        rc, out, _ = self.run_solution('ab', text, 'X')
        self.assertEqual(rc, 0)
        self.assertEqual(out, text.replace('ab', 'X'))

    def test_empty_replacement(self):
        rc, out, _ = self.run_solution('a', 'abcabc', '')
        self.assertEqual(rc, 0)
        self.assertEqual(out, 'bcbc')

if __name__ == '__main__':
    unittest.main()