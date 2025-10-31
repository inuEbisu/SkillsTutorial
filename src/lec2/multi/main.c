#include <stdio.h>
#include "greet.h"
#include "calc.h"

int main(void)
{
    // Use functions defined in other translation units (greet.c, calc.c)
    greet("Linux Learner");

    int x = 2, y = 3;
    printf("%d + %d = %d\n", x, y, add(x, y));

    int n = 10;
    printf("fib(%d) = %llu\n", n, fib(n));

    return 0;
}
