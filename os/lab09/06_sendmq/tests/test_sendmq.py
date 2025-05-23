import unittest
import subprocess
import os
import time

class TestSendMQ(unittest.TestCase):
    def setUp(self):
        self.bin = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sendmq'))
        self.queue = "/testmq_send"
        self.message = "Hello, MQ!"

        with open("crt_mq_tmp.c", "w") as f:
            f.write(f"""
#include <mqueue.h>
#include <fcntl.h>
#include <sys/stat.h>

int main() {{
    struct mq_attr attr = {{0}};
    attr.mq_maxmsg = 10;
    attr.mq_msgsize = 1024;
    mq_open("{self.queue}", O_CREAT | O_RDWR, 0600, &attr);
    return 0;
}}
""")
        subprocess.run(["gcc", "crt_mq_tmp.c", "-lrt", "-o", "crt_mq_tmp"], check=True)
        subprocess.run(["./crt_mq_tmp"], check=True)

    def tearDown(self):
        with open("unlink_queue.c", "w") as f:
            f.write(f"""
#include <mqueue.h>
int main() {{
    mq_unlink("{self.queue}");
    return 0;
}}
""")
        subprocess.run(["gcc", "unlink_queue.c", "-lrt", "-o", "unlink_queue"], check=True)
        subprocess.run(["./unlink_queue"], check=False)
        for file in ["crt_mq_tmp.c", "crt_mq_tmp", "unlink_queue.c", "unlink_queue"]:
            if os.path.exists(file):
                os.remove(file)

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