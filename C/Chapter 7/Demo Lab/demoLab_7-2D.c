/*  Conditional Statements
        Rochelle Gardner
        7 Feb 2019
        demoLab_7-2D.c
*/


#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>

int printMenu(void);

int main(void)
{	int number = 0;
	int menuSelection = 3;
	printf("Input an number:  ");
	scanf("%d", &number);

	do
	{	printMenu();									// call on the printMenu function
		scanf("%d", &menuSelection);
		switch (menuSelection)
		{	case 0:										// 1 - Exit
				printf("\n\nExiting...");
				break;
			case 1:										// 2 - Octal
				printf("Octal:  %o\n\n", number);
				break;
			case 2:										// 3 - Decimal
				printf("Decimal:  %d\n\n", number);
				break;
			case 3:										// 4 - Hexadecimal
				printf("Hexadecimal:  %X\n\n", number);
				break;
			case 4:										// 5 - Char
				printf("Character:  %c\n\n", number);
				break;
			case 5:										// 6 - New number
				printf("\n\nEnter a new number to display:  \n");
				scanf("%d", &number);
			
			default:
				break;
		}
	} while (menuSelection != 0);

	return 0;
}

int printMenu(void)
{	printf("How do you want to print that number?  \n\n");
	printf("1 - Octal \n2 - Decimal \n3 - Hexadecimal \n4 - Char \n5 - Enter a new number \n0 - Exit this program. \n\n\n");

	return 0;
}