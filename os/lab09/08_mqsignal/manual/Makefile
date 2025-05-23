CC = gcc
CFLAGS = -Wall -Wextra -std=c23 -lrt

all: snd_mq

snd_mq: snd_mq.c
	$(CC) $(CFLAGS) -o snd_mq snd_mq.c

clean:
	rm -f snd_mq