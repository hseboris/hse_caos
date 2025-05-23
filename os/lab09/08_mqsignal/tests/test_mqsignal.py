import unittest
import subprocess
import os
import time
import signal

class TestMQSignal(unittest.TestCase):
    def setUp(self):
        self.server_bin = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'mqsignal'))
        self.sender_bin = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'manual', 'snd_mq'))
        self.queue = "/mqsignal"

    def test_quit_message_stops_server(self):
        server = subprocess.Popen([self.server_bin], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        time.sleep(1)
        subprocess.run([self.sender_bin, self.queue, "hello"], check=True)
        time.sleep(0.5)
        subprocess.run([self.sender_bin, self.queue, "QUIT"], check=True)

        out, err = server.communicate(timeout=5)

        self.assertIn("Received: hello", out)
        self.assertIn("Server stopped", out)
        self.assertEqual(server.returncode, 0)

    def test_sigint_stops_server(self):
        server = subprocess.Popen([self.server_bin], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        time.sleep(1)
        subprocess.run([self.sender_bin, self.queue, "test"], check=True)
        time.sleep(0.5)
        os.kill(server.pid, signal.SIGINT)

        out, err = server.communicate(timeout=5)

        self.assertIn("Received: test", out)
        self.assertIn("Server stopped", out)
        self.assertEqual(server.returncode, 0)

if __name__ == '__main__':
    unittest.main()