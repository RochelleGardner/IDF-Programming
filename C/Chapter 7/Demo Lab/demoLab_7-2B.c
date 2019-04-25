/*  If-Else Statements
        Rochelle Gardner
        7 Feb 2019
        demoLab_7-2B.c
*/

#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>

int main(void)
{	int userInputNumber = 0;

	printf("Input a number:  \n");
	scanf("%d", &userInputNumber);

	if (userInputNumber & 1 == 1) 																		// If there is a remainder from num / 2 then it, by definition, is odd
	{	userInputNumber = userInputNumber * 2;															// If the number is odd, multiply the number by 2 and store the result in the original variable... */
		printf("The number was odd but I made it even. \nThe new number is %d. \n", userInputNumber);	// ...and print the new number
	}
	else
	{	printf("The number is even. \n");																// If the number is even, say so
	}

	return 0;
}