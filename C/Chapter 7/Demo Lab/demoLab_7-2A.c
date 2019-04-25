/*  IF Statements
        Rochelle Gardner
        7 Feb 2019
        demoLab_7-2A.c        
*/

#include <stdio.h>

int main(void)
{   char someArray[256] = {0};

    printf("Enter some words I guess: ");           // Ask user for input
    scanf("%255[^\n]s", someArray);                                             // Prompt input, limit to 255, kill on newline
    
    if (someArray[0] != 0)                                                      // Check for empty string
    {    printf("%s", someArray);
    }
    else                                                                        // Catch everything else
    {   printf("You didn't put in any words...");
    }

    return 0;
}