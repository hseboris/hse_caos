import unittest
import subprocess

class TestArrayReverse(unittest.TestCase):
    def run_array_rev(self, input_data):
        process = subprocess.Popen(
            ['./array_rev'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        output, err = process.communicate(input_data)
        return process.returncode, output.strip(), err.strip()

    def test_reverse_even(self):
        rc, out, _ = self.run_array_rev("4\n1 2 3 4\n")
        self.assertEqual(rc, 0)
        self.assertEqual(out, "4 3 2 1")

    def test_reverse_odd(self):
        rc, out, _ = self.run_array_rev("5\n10 20 30 40 50\n")
        self.assertEqual(rc, 0)
        self.assertEqual(out, "50 40 30 20 10")

    def test_single_element(self):
        rc, out, _ = self.run_array_rev("1\n99\n")
        self.assertEqual(rc, 0)
        self.assertEqual(out, "99")

    def test_empty_array(self):
        rc, out, _ = self.run_array_rev("0\n")
        self.assertEqual(rc, 0)
        self.assertEqual(out, "")

    def test_large_array(self):
        input_numbers = list(range(1000))
        input_str = f"{len(input_numbers)}\n" + " ".join(map(str, input_numbers)) + "\n"
        expected_output = " ".join(map(str, reversed(input_numbers)))
        rc, out, _ = self.run_array_rev(input_str)
        self.assertEqual(rc, 0)
        self.assertEqual(out, expected_output)

if __name__ == '__main__':
    unittest.main()