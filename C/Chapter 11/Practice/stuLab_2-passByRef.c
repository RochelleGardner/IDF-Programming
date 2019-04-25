/*  Pass by reference
    Rochelle Gardner
    21 Feb 2019
    stuLab_2-passByRef.c
*/

#include <stdio.h>

void cubeByReference (int *nPtr);   // prototype

int main (void)
{   int number = 5;     // initialize number
    
    printf ("The original value of number is %d", number);
    cubeByReference (&number);             // pass address of number to cubeByReference
    printf ("\nThe new value of number is %d\n", number);

}       // end of main

void cubeByReference (int *nPtr)    // calc cube of *nPtr; acrually modifies number in main();
{   *nPtr = *nPtr * *nPtr * *nPtr;  // cube of *nPtr
}       // end function cubeByReference