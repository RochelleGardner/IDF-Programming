#include <stdio.h>

 /* Performance Lab 2B
 *  This lab casts variable types and prints them out
 *  name: Rochelle Gardner
 *  date: 29 JAN 2019
 *  project: Lab 2B
 */

int main(void)                      // use this function to declare and print all variables
{   
    int num_1 = 56;                 // this is the  integer variable
    float float_1 = 2.3;            // this is the float variable
    double double_1 = 5.61;         // this is the double variable
    char chair = 'K';               // this is the character variable

    printf ("Your integer: %d cast to a float is: %f \n", num_1, (float)num_1);
    printf ("Your integer: %d cast to a char is: %c \n", num_1, (char)num_1);
    printf ("Your float: %f cast to a double is: %lf \n", float_1, (double)float_1);
    printf ("Your double: %lf cast to a float is: %f \n", double_1, (float)double_1);
    printf ("Your char: %c cast to an integer is: %d \n", chair, (int)chair);
    printf ("33 cast to a char is: %c \n", (char)33);

    return 0;

} 