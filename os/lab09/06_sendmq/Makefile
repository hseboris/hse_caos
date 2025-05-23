CC = gcc
CFLAGS = -Wall -Wextra -std=c2x -lrt

all: sendmq

sendmq: sendmq.c
	$(CC) $(CFLAGS) -o sendmq sendmq.c

clean:
	rm -f sendmq