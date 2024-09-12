#include <stdio.h>

void foo()
{
    printf("Hi Babe (^_^)/\n");
}

int main()
{
    int i = 10;
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