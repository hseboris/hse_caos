#include <mqueue.h>
#include <fcntl.h>
#include <sys/stat.h>

int main() {
    struct mq_attr attr = {0};
    attr.mq_maxmsg = 10;
    attr.mq_msgsize = 1024;
    mq_open("/testmq", O_CREAT | O_RDWR, 0600, &attr);
    return 0;
}