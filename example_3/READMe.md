# Example with Randomness
Due to randomness in the code you might get different results.

## Compile code 
```bash
afl-clang-fast -o example_3 main.c
```

## Generate execution path
```bash
afl-showmap -o cd_1_default.txt -m none -- ./example_3
afl-showmap -o cd_2_minus_10.txt -m none -- ./example_3 -10
afl-showmap -o cd_3_0.txt -m none -- ./example_3 0
afl-showmap -o cd_4_12.txt -m none -- ./example_3 12
afl-showmap -o cd_5_23.txt -m none -- ./example_3 23
```