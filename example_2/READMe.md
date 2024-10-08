# Example Accept Input

## Compile code 
```bash
afl-clang-fast -o example_2 main.c
```

## Generate execution path
```bash
afl-showmap -o cd_1_default.txt -m none -- ./example_2
afl-showmap -o cd_2_minus_10.txt -m none -- ./example_2 -10
afl-showmap -o cd_3_0.txt -m none -- ./example_2 0
afl-showmap -o cd_4_12.txt -m none -- ./example_2 12
afl-showmap -o cd_5_23.txt -m none -- ./example_2 23
```