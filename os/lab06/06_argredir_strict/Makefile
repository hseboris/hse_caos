CC = gcc
CFLAGS = -Wall -Wextra -std=c2x

all: argredir

argredir: argredir_strict.c
	$(CC) $(CFLAGS) -o argredir argredir_strict.c

clean:
	rm -f argredir input_strict.txt output_strict.txt