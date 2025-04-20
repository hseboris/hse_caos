import unittest
import subprocess

class TestListReverse(unittest.TestCase):
    def run_list_reverse(self, input_data):
        process = subprocess.Popen(
            ['./list_reverse'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        output, err = process.communicate(input_data)
        return process.returncode, output.strip(), err.strip()

    def test_reverse_basic(self):
        rc, out, _ = self.run_list_reverse("1 2 3 0\n")
        self.assertEqual(rc, 0)
        self.assertEqual(out, "3 2 1")

    def test_reverse_empty(self):
        rc, out, _ = self.run_list_reverse("0\n")
        self.assertEqual(rc, 0)
        self.assertEqual(out, "")

    def test_reverse_single(self):
        rc, out, _ = self.run_list_reverse("99 0\n")
        self.assertEqual(rc, 0)
        self.assertEqual(out, "99")

    def test_reverse_large(self):
        input_data = " ".join(map(str, range(1, 1001))) + " 0\n"
        expected_output = " ".join(map(str, range(1000, 0, -1)))
        rc, out, _ = self.run_list_reverse(input_data)
        self.assertEqual(rc, 0)
        self.assertEqual(out, expected_output)

if __name__ == '__main__':
    unittest.main()
