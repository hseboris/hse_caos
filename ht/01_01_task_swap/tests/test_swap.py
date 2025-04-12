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
        self.assertEqual(self.run_swap(3, 5), "After swap: x = 5, y = 3")

    def test_negative(self):
        self.assertEqual(self.run_swap(-1, 10), "After swap: x = 10, y = -1")

    def test_zero(self):
        self.assertEqual(self.run_swap(0, 0), "After swap: x = 0, y = 0")

    def test_large(self):
        self.assertEqual(self.run_swap(123456, 654321), "After swap: x = 654321, y = 123456")

    def test_equal(self):
        self.assertEqual(self.run_swap(42, 42), "After swap: x = 42, y = 42")

if __name__ == '__main__':
    unittest.main()