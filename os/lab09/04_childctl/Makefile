CC = gcc
CFLAGS = -Wall -Wextra -std=c2x

all: childctl

childctl: childctl.c
	$(CC) $(CFLAGS) -o childctl childctl.c

clean:
	rm -f childctl