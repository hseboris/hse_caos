import unittest
import subprocess

class TestSwapProgram(unittest.TestCase):
    def run_swap(self, x, y):
        result = subprocess.run(
            ["./swap"],
            input=f"{x} {y}",
            capture_output=True,
            text=True
        )
        return result.stdout.strip()

    def test_basic(self):
        self.assertEqual(self.run_swap(3, 5), "5 3")

    def test_negative(self):
        self.assertEqual(self.run_swap(-1, 10), "10 -1")

    def test_zero(self):
        self.assertEqual(self.run_swap(0, 0), "0 0")

    def test_large(self):
        self.assertEqual(self.run_swap(123456, 654321), "654321 123456")

    def test_equal(self):
        self.assertEqual(self.run_swap(42, 42), "42 42")

if __name__ == '__main__':
    unittest.main()
