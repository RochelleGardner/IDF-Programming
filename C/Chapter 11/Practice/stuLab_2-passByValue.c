/*  Pass by Value
    Rochelle Gardner
    21 Feb 2019
    stuLab_2.c
*/

#include <stdio.h>

int cubeByValue (int n);    // prototype

int main (void)
{   int number = 5;         // initialize number
    
    printf ("The original value of number is %d", number);
    number = cubeByValue (number);      // pass number by value to cubeByValue
    printf ("\nThe new value of number is %d\n", number);
    
}   // end of main

int cubeByValue (int n)     // calculate and return cube of integer argument
{   return n * n * n;       // cube local variable n and return result
}                           // end function cubeByValue