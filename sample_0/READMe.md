afl-clang-fast -o sample_0 main.c

afl-showmap -o cd.txt -m none -- ./sample_0