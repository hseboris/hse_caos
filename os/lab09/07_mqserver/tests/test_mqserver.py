import unittest
import subprocess
import os
import time

class TestMQServer(unittest.TestCase):
    def setUp(self):
        self.server_bin = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'mqserver'))
        self.sender_bin = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'manual', 'snd_mq'))
        self.queue = "/mqserver"

    def test_receive_and_quit(self):
        server = subprocess.Popen([self.server_bin], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        time.sleep(1)
        subprocess.run([self.sender_bin, self.queue, "hello"], check=True)
        time.sleep(0.5)
        subprocess.run([self.sender_bin, self.queue, "QUIT"], check=True)
        time.sleep(0.5)

        out, err = server.communicate(timeout=8)

        self.assertIn("Received: hello", out)
        self.assertNotIn("Received: QUIT", out)
        self.assertEqual(server.returncode, 0)

if __name__ == '__main__':
    unittest.main()