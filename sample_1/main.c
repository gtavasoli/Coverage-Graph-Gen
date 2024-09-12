#include <stdio.h>

void foo()
{
    printf("Hi (^_^)/\n");
}

int main(int argc, char *argv[])
{
    int i;
    if (argc > 1)
    {
        sscanf(argv[1], "%d", &i);
    }
    else
    {
        i = 10;
    }
    printf("Start...\n");
    while (i-- > 0)
    {
        printf("I = %d\n", i);
        if (i % 2 == 0)
            foo();
    }
    printf("It is done\n");
    return 0;
}
