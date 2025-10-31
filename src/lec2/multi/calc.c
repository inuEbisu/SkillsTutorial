#include "calc.h"

int add(int a, int b)
{
    return a + b;
}

unsigned long long fib(int n)
{
    if (n < 0)
        return 0; // simple guard; not expected for teaching demo
    unsigned long long a = 0, b = 1;
    for (int i = 0; i < n; ++i)
    {
        unsigned long long next = a + b;
        a = b;
        b = next;
    }
    return a;
}
