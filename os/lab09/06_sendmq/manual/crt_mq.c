#include <mqueue.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <stdio.h>
#include <stdlib.h>

int main() {
    struct mq_attr attr;
    attr.mq_maxmsg = 10;
    attr.mq_msgsize = 1024;
    attr.mq_flags = 0;

    mqd_t mqd = mq_open("/testmq", O_CREAT | O_RDWR, 0600, &attr);
    if (mqd == (mqd_t)-1) {
        perror("mq_open");
        return 1;
    }

    mq_close(mqd);
    return 0;
}