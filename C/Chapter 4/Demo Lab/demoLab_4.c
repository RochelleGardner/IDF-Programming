#define _CRT_SECURE_NO_WARNINGS 1            // Disables warning
#include <stdio.h>                           // Standard IO header

int main(void)
{
    char buff[4];
    printf ("Enter a string: ");
    fgets (buff, sizeof(buff), stdin);
    printf ("Your string was: ");
    fputs (buff, stdout);

    return 0;

}