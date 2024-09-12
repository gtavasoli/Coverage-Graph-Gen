
Due to randomness in the code you might get different results.

afl-clang-fast -o sample_2 main.c

afl-showmap -o cd_1_default.txt -m none -- ./sample_2
afl-showmap -o cd_2_minus_10.txt -m none -- ./sample_2 -10
afl-showmap -o cd_3_0.txt -m none -- ./sample_2 0
afl-showmap -o cd_4_12.txt -m none -- ./sample_2 12
afl-showmap -o cd_5_23.txt -m none -- ./sample_2 23