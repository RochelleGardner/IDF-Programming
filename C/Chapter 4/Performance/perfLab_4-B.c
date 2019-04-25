/*  
*       Performance Lab 2: Chapter 4
*       Rochelle Gardner
*       2 Feb 2019
*       perfLab_4-B
*/

#include <stdio.h>

int main (void)
{
	int userSaid = 0;                                   // initialize vatiable for user input
	printf("Enter a character:  ");                     // prompt user for input
	userSaid = getc(stdin);                             // store the user's input
	printf("The next character sequentially is:  ");    // display
	putc(userSaid - 1, stdout);                         // increment user's character by one

    return 0;
}
