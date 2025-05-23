import unittest
import subprocess
import os
import time

class TestSendMQ(unittest.TestCase):
    def setUp(self):
        self.sendmq = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sendmq'))
        self.queue = "/testmq_send"
        self.message = "Hello, MQ!"

        # компилируем и запускаем crt_mq.c из лекции
        with open("crt_mq_tmp.c", "w") as f:
            f.write("""
#include <mqueue.h>
#include <fcntl.h>
#include <sys/stat.h>

int main() {
    struct mq_attr attr = {0};
    attr.mq_maxmsg = 10;
    attr.mq_msgsize = 1024;
    mq_open(\"/testmq_send\", O_CREAT | O_RDWR, 0600, &attr);
    return 0;
}
""")
        subprocess.run(["gcc", "crt_mq_tmp.c", "-lrt", "-o", "crt_mq_tmp"], check=True)
        subprocess.run(["./crt_mq_tmp"], check=True)

    def tearDown(self):
        subprocess.run(["rm", "-f", "crt_mq_tmp", "crt_mq_tmp.c"])
        subprocess.run(["mq_unlink", self.queue], stderr=subprocess.DEVNULL)

    def test_send_message_success(self):
        result = subprocess.run(
            [self.sendmq, self.queue, self.message],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr.strip(), "")

    def test_send_invalid_queue(self):
        result = subprocess.run(
            [self.sendmq, "/doesnotexist", self.message],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("mq_open", result.stderr)

if __name__ == '__main__':
    unittest.main()