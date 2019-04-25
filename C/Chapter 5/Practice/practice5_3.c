/*      Relational Operators Quiz
*       Rochelle Garnder
*       2 Feb 2019
*       practice_2.c
*/

#include <stdio.h>
#include <math.h>

int main (void)
{
    int x = 2;
    int y = 6;

    printf ("\nX is 2\nY is 6:\n");   
    printf ("\t0 means False 1 means True\n");
    printf ("\ty < x :\t\t\t%i\n", y < x);                          // y < x
    printf ("\ty <=x :\t\t\t%i\n", y <=x);                          // y <=x
    printf ("\ty > x :\t\t\t%i\n", y > x);                          // y > x
    printf ("\ty >= x :\t\t%i\n", y >= x);                          // y >= x
    printf ("\ty == x :\t\t%i\n", y == x);                          // y == x
    printf ("\ty != x :\t\t%i\n", y != x);                          // y != x
    printf ("\t2 == y :\t\t%i\n", 2 == y);                          // 2 == y
    printf ("\t6 != y :\t\t%i\n", 6 != y);                          // 6 != y
    printf ("\t6 >= 2 :\t\t%i\n", 6 >= 2);                          // 6 >= 2
    printf ("\t2 < 6 :\t\t\t%i\n", 2 < 6);                          // 2 < 6
    printf ("\tx != y != 3 >= x :\t%i\n", (x != y != 3 >= x));      // x != y != 3 >= x

    return 0;
}