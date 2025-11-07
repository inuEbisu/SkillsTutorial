#include <stdio.h>
#include <unistd.h>

int main(void) {
    // freopen("data.in", "r", stdin);
    // freopen("data.out", "w", stdout);

    char c;
    while((c = getchar()) != -1) {
        putchar(c);
        sleep(20);
    }
    
    return 0;
}