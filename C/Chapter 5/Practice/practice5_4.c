/*      Logical Operators Quiz
*       Rochelle Garnder
*       2 Feb 2019
*       practice5_3.c
*/

#include <stdio.h>

int main (void)
{
    int x = 99;
    int y = 0;

    printf ("\nX is 99\nY is 0:\n");   
    printf ("\t0 means False 1 means True\n");
    printf ("\tx AND y:\t\t%i\n", x&&y);                                // x && y               False
    printf ("\ty OR x:\t\t\t%i\n", y||x);                               // y || x               True
    printf ("\tNOT y:\t\t\t%i\n", !y);                                  // !y                   True
    printf ("\ty AND 0:\t\t%i\n", y&&0);                                // y && 0               False
    printf ("\tx OR 42:\t\t%i\n", x||42);                               // x || 42              True
    printf ("\tNOT x:\t\t\t%i\n", !x);                                  // !x                   False
    printf ("\tx AND x:\t\t%i\n", x&&x);                                // x && x               True
    printf ("\ty OR y:\t\t\t%i\n", y||y);                               // y || y               False
    printf ("\tNOT 1:\t\t\t%i\n", !1);                                  // !1                   False
    printf ("\t1 AND 1:\t\t%i\n", 1&&1);                                // 1 && 1               True
    printf ("\t(0 AND 1) OR (2 AND 3):\t%i\n\n", ((0&&1)||(2&&3)));     // (0 && 1)||(2 && 3)   True

    return 0;
}