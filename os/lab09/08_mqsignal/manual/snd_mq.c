#include <mqueue.h>
#include <fcntl.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

int main(int argc, char *argv[]) {
    if (argc != 3) {
        fprintf(stderr, "Usage: %s /queue message\n", argv[0]);
        return 1;
    }

    mqd_t mqd = mq_open(argv[1], O_WRONLY);
    if (mqd == (mqd_t)-1) {
        perror("mq_open");
        return 1;
    }

    if (mq_send(mqd, argv[2], strlen(argv[2]), 1) == -1) {
        perror("mq_send");
        mq_close(mqd);
        return 1;
    }

    mq_close(mqd);
    return 0;
}