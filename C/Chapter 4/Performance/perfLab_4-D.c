/*  
*       Performance Lab 4: Chapter 4
*       Rochelle Gardner
*       2 Feb 2019
*       perfLab_4-D
*/

#include <stdio.h>

int main (void)
{
    char first [32] = {0};
    char middle [32] = {0};
    char last [32] = {0};

    int num1 = 0;
    int num2 = 0;

    printf ("Enter your full name separated by tabs: ");
    scanf ("%32s\t%32s\t%32s", &first, &middle, &last);

    printf ("Enter two integers, separated by a *, to be multiplied: ");
    scanf ("%d*%d", &num1, &num2);

    printf ("Your name is: \t\n%s\t\n%s\t\n%s\t\n", first, middle, last);
    int num3 = (num1*num2);
    printf ("The result of %d multiplied by %d is %d", num1, num2, num3);


    return 0;
}
