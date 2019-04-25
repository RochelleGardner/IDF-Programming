/*
*   Practice ch0_4 fscanf()
*       Rochelle Gardner
*       2 Feb 2019
*       practice_4-8
*/

#include <stdio.h>

int main (void)
{
    int theAnswer = 42;
    float pi = 3.141592;
    double posSqrtTwo = 1.41421356237;
    char answerNum1 [] = 63;
    fscanf(stdin, “%d”, &theAnswer);            // Reads an integer from stdin
    fscanf(stdin, “%f”, &pi);                   // Reads a float from stdin
    fscanf(stdin, “%lf”, &posSqrtTwo);          // Reads a double from stdin
    fscanf(stdin, “%c”, &answerNum1);           // Reads a character from stdin

    char nickName[20] = {0};
    fscanf(stdin, “%s”, nickName);              // Still dangerous
    fscanf(stdin, “%19s”, nickName);            // Safer string read from stdin

    return 0;
}