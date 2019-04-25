#include <stdio.h>
#include <string.h>

/*  Performance Lab 3B
*   Author: Rochelle Gardner
*   Date: 30 JAN 2019
*   Project: perfLab_3B
*/

int main (void)
{
    char myCharArray [256] = {0};   //zeroized array
    myCharArray [0] = 'P';
    myCharArray [1] = 's';
    myCharArray [2] = 'e';
    myCharArray [3] = 'u';
    myCharArray [4] = 'd';
    myCharArray [5] = 'o';
    myCharArray [6] = 'n';
    myCharArray [7] = 'y';
    myCharArray [8] = 'm';
    myCharArray [9] = '\0';         //null character to end the string

    printf ("My saying is: %s\n", myCharArray);
    printf ("The length of my saying is: %d\n", (strlen(myCharArray)));

    return 0;

}