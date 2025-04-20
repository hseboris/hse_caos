import unittest
import subprocess

class TestMatrixTranspose(unittest.TestCase):
    def run_transpose(self, input_data):
        proc = subprocess.Popen(
            ['./matrix_transpose'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        out, err = proc.communicate(input_data)
        return proc.returncode, out.strip(), err.strip()

    def test_square(self):
        inp = "2 2\n1 2\n3 4\n"
        rc, out, _ = self.run_transpose(inp)
        self.assertEqual(rc, 0)
        self.assertEqual(out, "1 3\n2 4")

    def test_rectangle(self):
        inp = "2 3\n1 2 3\n4 5 6\n"
        rc, out, _ = self.run_transpose(inp)
        self.assertEqual(rc, 0)
        self.assertEqual(out, "1 4\n2 5\n3 6")

    def test_single_row(self):
        inp = "1 4\n7 8 9 10\n"
        rc, out, _ = self.run_transpose(inp)
        self.assertEqual(rc, 0)
        self.assertEqual(out, "7\n8\n9\n10")

    def test_single_col(self):
        inp = "4 1\n1\n2\n3\n4\n"
        rc, out, _ = self.run_transpose(inp)
        self.assertEqual(rc, 0)
        self.assertEqual(out, "1 2 3 4")

    def test_empty(self):
        inp = "0 0\n"
        rc, out, _ = self.run_transpose(inp)
        self.assertEqual(rc, 0)
        self.assertEqual(out, "")

    def test_large_square(self):
        # 50×50
        N = M = 50
        mat = [[i*M + j for j in range(M)] for i in range(N)]
        inp = f"{N} {M}\n" + "\n".join(" ".join(map(str, row)) for row in mat) + "\n"
        # transpose in Python
        transposed = list(zip(*mat))
        expected = "\n".join(" ".join(map(str, row)) for row in transposed)
        rc, out, _ = self.run_transpose(inp)
        self.assertEqual(rc, 0)
        self.assertEqual(out, expected)

    def test_large_rectangular(self):
        # 30×10
        N, M = 30, 10
        mat = [[i*M + j for j in range(M)] for i in range(N)]
        inp = f"{N} {M}\n" + "\n".join(" ".join(map(str, row)) for row in mat) + "\n"
        transposed = list(zip(*mat))
        expected = "\n".join(" ".join(map(str, row)) for row in transposed)
        rc, out, _ = self.run_transpose(inp)
        self.assertEqual(rc, 0)
        self.assertEqual(out, expected)


if __name__ == '__main__':
    unittest.main()