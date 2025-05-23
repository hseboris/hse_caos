CC = gcc
CFLAGS = -Wall -Wextra -std=c2x -lrt

all: crt_mq rec_mq

crt_mq: crt_mq.c
	$(CC) $(CFLAGS) -o crt_mq crt_mq.c

rec_mq: rec_mq.c
	$(CC) $(CFLAGS) -o rec_mq rec_mq.c

clean:
	rm -f crt_mq rec_mq