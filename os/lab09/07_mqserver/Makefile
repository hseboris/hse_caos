CC = gcc
CFLAGS = -Wall -Wextra -std=c2x -lrt

all: mqserver

mqserver: mqserver.c
	$(CC) $(CFLAGS) -o mqserver mqserver.c

clean:
	rm -f mqserver