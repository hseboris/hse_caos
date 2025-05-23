#include <mqueue.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>

int main() {
    mqd_t mqd;
    unsigned int prio;
    struct mq_attr attr;
    void *buf;
    ssize_t n;

    mqd = mq_open("/testmq", O_RDONLY);
    if (mqd == (mqd_t)-1) {
        perror("mq_open");
        return 1;
    }

    if (mq_getattr(mqd, &attr) == -1) {
        perror("mq_getattr");
        mq_close(mqd);
        return 1;
    }

    buf = malloc(attr.mq_msgsize);
    if (!buf) {
        perror("malloc");
        mq_close(mqd);
        return 1;
    }

    n = mq_receive(mqd, buf, attr.mq_msgsize, &prio);
    if (n == -1) {
        perror("mq_receive");
        free(buf);
        mq_close(mqd);
        return 1;
    }

    printf("Received: %s\nPriority: %u\n", (char *)buf, prio);
    free(buf);
    mq_close(mqd);
    return 0;
}