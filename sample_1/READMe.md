afl-clang-fast -o sample_1 main.c

afl-showmap -o cd_1_default.txt -m none -- ./sample_1
afl-showmap -o cd_2_minus_10.txt -m none -- ./sample_1 -10
afl-showmap -o cd_3_0.txt -m none -- ./sample_1 0
afl-showmap -o cd_4_12.txt -m none -- ./sample_1 12
afl-showmap -o cd_5_23.txt -m none -- ./sample_1 23