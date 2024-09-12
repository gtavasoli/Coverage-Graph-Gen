#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void foo(int x)
{
    printf("In foo with x = %d\n", x);
}

void bar(int y)
{
    if (y % 2 == 0)
    {
        printf("Even y in bar: %d\n", y);
    }
    else
    {
        printf("Odd y in bar: %d\n", y);
    }
}

int main(int argc, char *argv[])
{
    srand(time(NULL)); // Initialize random seed

    int i = 10;
    if (argc > 1)
    {
        sscanf(argv[1], "%d", &i); // Get input from the user
    }

    printf("Starting program with i = %d\n", i);

    // Outer loop with a dynamic stopping condition
    while (i-- > 0)
    {
        printf("i = %d\n", i);

        if (i % 2 == 0)
        {
            foo(i); // Call foo for even i
        }
        else
        {
            bar(i); // Call bar for odd i
        }

        // Inner loop, adding more complexity
        int j = rand() % 5; // Random number between 0 and 4
        while (j-- > 0)
        {
            printf("Inner loop j = %d\n", j);
            if (j == 2)
            {
                printf("Special case for j == 2\n");
            }
        }

        // Add another condition for more branches
        if (i == 5)
        {
            printf("i is exactly 5!\n");
        }
    }

    printf("Program is done.\n");
    return 0;
}
