/*      Assignment Operators Quiz
*       Rochelle Garnder
*       2 Feb 2019
*       practice5_4.c
*/

#include <stdio.h>
#include <math.h>

int main (void)
{
    int x = 9;
    int y = 3;

    printf ("\nX is 9\nY is 3:\n");
    printf ("\tx *= y:\t\t%i\n", x*-y);                                     // x *= y
    printf ("\tx /= y:\t\t%i\n", x/=y);                                     // x /= y       
    printf ("\tx %%= y:\t\t%i\n", x%=y);                                    // x %= y
    printf ("\tx += y:\t\t%i\n", x+=y);                                     // x += y
    printf ("\tx -= y:\t\t%i\n", x-=y);                                     // x -= y
    printf ("\tx *= ++y:\t%i\n", x*=++y);                                   // x*= ++y
    printf ("\tx /= y--:\t%i\n", x/=y--);                                   // x /= y--
    printf ("\tx %%= --x:\t%i\n", x%=--x);                                  // x %= --x
    printf ("\tx += --y:\t%i\n", x+=--y);                                   // x += --y
    printf ("\tx -= y++:\t%i\n", x-=y++);                                   // x -= y++
    printf ("\t(y %%= y)||(x /= x--):\t%i\n\n", ((y%=y)||(x/=x--)));          // (y %= y)||(x /= x--)

    return 0;
}
