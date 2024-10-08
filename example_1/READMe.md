# Simple Example

## Compile code 
```bash
afl-clang-fast -o example_1 main.c
```

## Generate execution path
```bash
afl-showmap -o cd.txt -m none -- ./example_1
```