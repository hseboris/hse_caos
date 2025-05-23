CC = gcc
CFLAGS = -Wall -Wextra -std=c2x -lrt

all: mqsignal

mqsignal: mqsignal.c
	$(CC) $(CFLAGS) -o mqsignal mqsignal.c

clean:
	rm -f mqsignal