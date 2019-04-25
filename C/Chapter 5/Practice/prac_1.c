/*      Arithmetic Operators Quiz
*       Rochelle Garnder
*       2 Feb 2019
*       practice_1.c
*/

#include <stdio.h>

int main (void)
{
    int x = 7;
    int y = 4;
    float z = 0.00;

    printf ("\nX is 7\nY is 4:\n");
    printf ("\tx * y = %.4lf\n", (double)(x*y));
    printf ("\t%4.4lf = x / y\n", (double)(x/y));
    printf ("\tx %% y = %d\n", (x%y));
    printf ("\ty + x = %d\n", (y+x));
    printf ("\ty - x = %d\n", (y-x));
    printf ("\t-y = %d\n", (-y));
    printf ("\t++x = %d\n", (++x));
    printf ("\ty++ = %d\n", (y++));
    printf ("\tx-- = %d\n", (x--));
    printf ("\t--y = %d\n", (--y));
    printf ("\t1 + 2 * (3 + %d) + 5 = %.4f\n\n",y,(float)(x*y));

    return 0;
}