import unittest
import subprocess

class TestSolution(unittest.TestCase):
    def run_solution(self):
        process = subprocess.Popen(
            ['./solution'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        output, err = process.communicate()
        return process.returncode, output.strip(), err.strip()

    def test_output(self):
        rc, out, err = self.run_solution()

        self.assertEqual(rc, 0, msg=f"Program exited with code {rc}, stderr: {err}")

        expected_outputs = [
            "bill: you passed Hello World!",
            "fred: you passed 42",
            "john: sqrt(16.000000) = 4.000000",
            "sam: cos(3.141590) = -1.000000"
        ]

        for expected in expected_outputs:
            self.assertIn(expected, out, msg=f"Expected '{expected}' in output, but not found.\nFull output:\n{out}")

if __name__ == '__main__':
    unittest.main()