CC = gcc
CFLAGS = -Wall -Wextra -std=c2x

all: matrix_transpose

matrix_transpose: solution.c
	$(CC) $(CFLAGS) -o matrix_transpose $<

clean:
	rm -f matrix_transpose