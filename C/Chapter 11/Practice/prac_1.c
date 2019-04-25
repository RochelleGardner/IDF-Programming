/*  a. Define the variable fPtr to be a pointer to an object of type foat
    b. Assign the address of variable number1 to pointer variable fPtr.
    c. Print the value of the object pointed to by fPtr.
    d. Assign the value of the object pointed to by fPtr to variable number2.
    e. Print the value of number2.
    f. Print the address of number 1.
    g. Print the address stored in fPtr. Use the %p conversion specifier.
        Is the value printed the same as the address of number1?

    Practice 1
    Rochelle Gardner
    21 Feb 2019
    prac_1.c
*/

#include <stdio.h>

int main (void)
{   float number1 = 7.3;
    float number2 = 0.0;
    float * int_fPtr;
    int_fPtr = &number1;
    number2 = *int_fPtr;
    *int_fPtr = 1;

    printf ("\nThe value of number2 is %f\n", number2);
    printf ("The address of number1 is %p\n", number1);
    printf ("The address stored in fPtr is %p\n\n", int_fPtr);

    return 0;
}