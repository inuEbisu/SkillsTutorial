#include <stdio.h>
#include "greet.h"

void greet(const char *name)
{
    if (!name || !*name)
    {
        name = "World";
    }
    printf("Hello, %s!\n", name);
}
