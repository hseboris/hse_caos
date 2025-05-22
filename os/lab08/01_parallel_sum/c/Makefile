CC = gcc
CFLAGS = -Wall -Wextra -std=c2x -lpthread

all: sum_threads

sum_threads: sum_threads.c
	$(CC) $(CFLAGS) -o sum_threads sum_threads.c

clean:
	rm -f sum_threads