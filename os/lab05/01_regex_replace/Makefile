CC = gcc
CFLAGS = -Wall -Wextra -std=c11 -g
TARGET = solution

.PHONY: all clean

all: $(TARGET)

$(TARGET): solution.o
	$(CC) -o $(TARGET) solution.o -Wall -Wextra -std=c11 -lm

solution.o: solution.c
	$(CC) $(CFLAGS) -c solution.c

clean:
	rm -f *.o $(TARGET)