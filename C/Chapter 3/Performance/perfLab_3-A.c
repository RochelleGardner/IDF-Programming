#include <stdio.h>

/*  Demonstration Lab 1
*   Author: Rochelle Gardner
*   Date: 30 JAN 2019
*   Project: demolab_1-3.c
*/

int main (void)
{
    int i = 1;                      // iterating variable
    int numStudents [15] = {0};     // declare and zeroize int array with dim = number of students +1
    numStudents [0] = 29;           // set instructor age at index 0 
    numStudents [i] = 20;
    numStudents [i + 1] = 22;
    numStudents [i + 2] = 23;
    numStudents [i + 3] = 21;
    numStudents [i + 4] = 20;
    numStudents [i + 5] = 23;
    numStudents [i + 6] = 23;
    numStudents [i + 7] = 22;
    numStudents [i + 8] = 26;
    numStudents [i + 9] = 25;
    numStudents [i + 10] = 21;
    numStudents [i + 11] = 22;
    numStudents [i + 12] = 24;
    numStudents [i + 13] = 23;
    numStudents [i + 14] = 20;

    printf ("The class ages are: \n");
    for (i = 1; i < 15; i++)
    {
        printf ("Student %d is %d years old. \n", i+1, numStudents[i]);
    }

    char sayStuff [] = {'W', 'H', 'Y',' ', 'N', 'O', 'T', '?'};
    for (i = 0; i < 8, i++)
    {
        printf ("%c", sayStuff[i]);
    
    }

    return 0;

}