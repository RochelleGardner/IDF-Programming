/*      Arithmetic Operators Quiz
*       Rochelle Garnder
*       2 Feb 2019
*       practice_1.c
*/

#include <stdio.h>
#include <math.h>

int x = 7;
int y = 4;
float z = 0.00;

int main (void)
{
    int x = 7;
    int y = 4;
    float z = 0.00;

    printf ("\nX is 7\nY is 4:\n");                                 // 
    printf ("\tx * y = %.4lf\n", (double)(x*y));                    // y * x = 28
    printf ("\t%.4lf = x / y\n", (double)(x/y));                    // 1.75 = x / y
    printf ("\tx %% y = %d\n", (x%y));                              // x % y = 3
    printf ("\ty + x = %d\n", (y+x));                               // y + x = 11
    printf ("\ty - x = %d\n", (y-x));                               // y - x = -3
    printf ("\t-y = %d\n", (-y));                                   // -y = -4
    printf ("\t++x = %d\n", (++x));                                 // ++x = 8
    printf ("\ty++ = %d\n", (y++));                                 // y++ = 4
    printf ("\tx-- = %d\n", (x--));                                 // x-- = 8
    printf ("\t--y = %d\n", (--y));                                 // --y = 4
    printf ("\t1 + 2 * (3 + %d) + 5 = %.4f\n\n",y,(float)(x*y));    // 1 + 2 * (3 + y) + 5 = 28

    return 0;
}