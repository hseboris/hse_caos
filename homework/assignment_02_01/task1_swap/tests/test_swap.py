import unittest
import subprocess

class TestSwap(unittest.TestCase):
    def run_swap(self, inp):
        """
        Запускает программу ./swap с данным вводом,
        возвращает кортеж (returncode, stdout, stderr).
        """
        p = subprocess.Popen(
            ['./swap'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        out, err = p.communicate(inp)
        return p.returncode, out.strip(), err.strip()

    def test_positive_numbers(self):
        rc, out, err = self.run_swap("1 2\n")
        self.assertEqual(rc, 0, "Программа завершилась с ошибкой")
        self.assertEqual(out, "2 1")

    def test_negative_and_positive(self):
        rc, out, err = self.run_swap("-5 10\n")
        self.assertEqual(rc, 0)
        self.assertEqual(out, "10 -5")

    def test_zero_and_positive(self):
        rc, out, err = self.run_swap("0 123\n")
        self.assertEqual(rc, 0)
        self.assertEqual(out, "123 0")

    def test_same_value(self):
        rc, out, err = self.run_swap("7 7\n")
        self.assertEqual(rc, 0)
        self.assertEqual(out, "7 7")

    def test_large_values(self):
        # Проверяем границы 32‑битных int
        rc, out, err = self.run_swap("2147483647 -2147483648\n")
        self.assertEqual(rc, 0)
        self.assertEqual(out, "-2147483648 2147483647")

if __name__ == '__main__':
    unittest.main()
