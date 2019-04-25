#include <stdio.h>

/*  Demolab 4-3
*   Name: Rochelle Gardner
*   Date: 1 Feb 2019
*   Proj: Demolab_1.c
*/

int main (void)
{
    int getchar();                          // initialize the getchar function to nothing
    int putchar();                          // initialize the putchar function to nothing
    int userSaid = 0;                       // initialize "userSaid" with the value of 0 as a placeholder for an argument provided later
    printf ("Enter your character: ");      // prompt the user
    userSaid = getchar();                   // store user input into userSaid using the getchar() function
    printf ("Your character was: ");        // preface the display user input
    putchar(userSaid);                      // display the variable userSaid with the new value of whatever the user input was

    return 0;                               // return 0 to exit cleanly

}