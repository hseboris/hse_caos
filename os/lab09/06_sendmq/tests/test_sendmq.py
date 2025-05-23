import unittest
import subprocess
import os
import time

class TestSendMQ(unittest.TestCase):
    def setUp(self):
        self.bin = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sendmq'))
        self.queue = "/testmq_send"
        self.message = "Test Message"

        # Создать очередь
        subprocess.run([
            "mq_open", self.queue, "O_CREAT|O_RDWR", "0600", "10", "1024"
        ], stderr=subprocess.DEVNULL)

    def tearDown(self):
        try:
            subprocess.run(["mq_unlink", self.queue], stderr=subprocess.DEVNULL)
        except:
            pass

    def test_send_message_success(self):
        result = subprocess.run(
            [self.bin, self.queue, self.message],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr.strip(), "")

    def test_send_invalid_queue(self):
        result = subprocess.run(
            [self.bin, "/doesnotexist", self.message],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("mq_open", result.stderr)

if __name__ == '__main__':
    unittest.main()