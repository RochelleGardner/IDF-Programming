#include <stdio.h>

/*  DemoLab 4-4
*   Name: Rochelle Gardner
*   Date: 1 Feb 2019
*   Proj: demoLab_2.c
*/

int main (void)
{
    int getc(FILE *stream);
    int putc(int char, FILE *stream);
    int userSaid = 0;
    printf ("Enter your character: ");
    userSaid = getc(stdin);
    printf ("Your character was: ");
    putc (userSaid, stdout);
    
    return 0;

}