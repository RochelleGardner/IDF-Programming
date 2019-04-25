#include <stdio.h>

/*  Demonstration Lab 1
*   Author: Rochelle Gardner
*   Date: 30 JAN 2019
*   Project: demolab_1-3.c
*/

int main (void)
{ 
    int myIntArray [10] = {100, 100, 100, 100, 100, 100, 100, 100, 100, 100};
    float myFloatArray [5] = {1, 2, 3, 4, 5};
    char myCharArray [256] = {0};

    printf ("The 3rd index in myIntArray is: %d \n", myIntArray[2]);
    printf ("The 3rd index in myFloatArray is: %f \n", myFloatArray[2]);
    printf ("The 3rd index in myCharArray is: %c \n", myCharArray[2]);

    return 0;

}