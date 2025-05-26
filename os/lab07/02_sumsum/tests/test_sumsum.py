import unittest
import subprocess
import os

class TestSumSum(unittest.TestCase):
    def setUp(self):
        self.script = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sumsum.sh'))
        os.chmod(self.script, 0o755)

    def run_case(self, input_lines, expected):
        result = subprocess.run(
            [self.script],
            input=input_lines,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), expected)

    def test_case_1(self):
        self.run_case("1 3 5\n2 4 6\n", "Not equal")

    def test_case_2(self):
        self.run_case("1 5 6\n4 4 4\n", "Equal")

    def test_case_3(self):
        self.run_case("1 2 w\n3 4 e\n", "Equal")

    def test_case_4(self):
        self.run_case("1 2 1\n2 2 Q\n", "Not equal")

    def test_case_5(self):
        self.run_case("qwe 3 4\n10 20 -30\n", "Equal")

    def test_large_input_with_error(self):
        line1 = " ".join(str(i) for i in range(100))        # сумма 0..99 = 4950
        line2 = " ".join(str(i) for i in range(98)) + " X Y" # ошибка → 0
        self.run_case(f"{line1}\n{line2}\n", "Not equal")

if __name__ == '__main__':
    unittest.main()