#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

int main(int argc, char *argv[]) {
    if (argc < 3) {
        fprintf(stderr, "Usage: %s command [args...] output_file\n", argv[0]);
        exit(1);
    }

    // output file is last argument
    char *output_file = argv[argc - 1];

    int fd = open(output_file, O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (fd < 0) {
        perror("open");
        exit(1);
    }

    if (dup2(fd, STDOUT_FILENO) < 0) {
        perror("dup2");
        exit(1);
    }

    close(fd);

    // prepare argument list: command + args (excluding output filename)
    argv[argc - 1] = NULL;

    execvp(argv[1], &argv[1]);
    perror("execvp");
    exit(1);
}