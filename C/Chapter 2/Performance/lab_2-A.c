/* This is the variable declarations script
*
*   name: Rochelle Gardner
*   date: 29 JAN 2019
*   project: variable declarations
*
*/
#include <stdio.h>

int main(void)              // this is where I initialize all my variables and print them
{
    int num_1 = 1;          // this is the integer variable
    float num_2 = 1.1;      // this is the float variable
    double num_3 = 1.11;    // this is the double variable
    char let_1 = '!';       // this is the char variable

    printf ("Int is %d \n", num_1);
    printf ("Size of int is %d \n", sizeof(num_1));
    printf ("Float is %f \n", num_2);
    printf ("Size of float is %d \n", sizeof (num_2));
    printf ("Double is %f \n", num_3);
    printf ("Size of double is %d \n", sizeof (num_3));
    printf ("Char is %c \n", let_1);
    printf ("Size of char is %d \n", sizeof (let_1));

    return 0;
}