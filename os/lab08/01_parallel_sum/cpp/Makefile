CXX = g++
CXXFLAGS = -Wall -Wextra -std=c++23 -pthread

all: sum_threads

sum_threads: sum_threads.cpp
	$(CXX) $(CXXFLAGS) -o sum_threads sum_threads.cpp

clean:
	rm -f sum_threads