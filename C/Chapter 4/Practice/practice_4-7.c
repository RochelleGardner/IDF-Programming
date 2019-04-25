#include <stdio.h>

int main (void) 
{
    int num1 = 0;
    int num2 = 0;
    double GPA = 3.7;
    double posSqrtTwo = 1.41421356;
    char ansNum1 [] = {'a','b','c','d'};
    char capsChar [] = {"A-Z"};
    int rngOfChar = 0;
    int binaryStr = 0;
    char Gadsby [256] = {0};

    scanf ("%d,%d", &num1, &num2);
    scanf ("%3f", &GPA);
    scanf ("*%lf", &posSqrtTwo);
    scanf ("%[abcd]c", &ansNum1);
    scanf ("%[A-Z]c", &capsChar);
    scanf ("%[A-z]c", &rngOfChar);
    scanf ("%32[01]s", binaryStr);
    scanf ("%64[^e\n]s", Gadsby);

    return 0;
}
