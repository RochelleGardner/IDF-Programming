/*  Conditional Statements
        Rochelle Gardner
        7 Feb 2019
        demoLab_7-2C.c
*/

#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
#include <inttypes.h>

int main(void)
{	int variable1 = 0;													// Initialize three int variables to 0
	int variable2 = 0;
	int variable3 = 0;
																		
	printf ("Enter two integers separated by a single space. \n");		// Safely scan user input into the variable #1 and #2 utilizing a single line
	printf ("(e.g., -17 1932) \n");
	scanf  ("%d %d", &variable1, &variable2);
	printf ("\n1. If your two numbers are equal, Variable 3 will be 0.\n");
	printf ("2. If your first number is bigger than the second, subtract the second number from it.\n");
	printf ("3. If your second number is bigger than the first, subtract the first number from it.\n");
	printf ("\t-If the result is negative, an error will print.\n");
	printf ("4. Otherwise you broke it.\n\n");

	if (variable1 == variable2) 										// Executes this block if the two input variables are equal
	{	variable3 = 0;	
	}
	else if (variable1 > variable2) 									// Executes this block if variable1 is the largest
	{	variable3 = variable1 - variable2; 								// Variable1 is larger so this statement subtracts variable2 and assigns the result to variable3					
	}
	else																// Executes this block if variable 2 is the largest
	{	variable3 = variable2 - variable1; 								// Variable2 is larger so this statement subtracts variable1 and assigns the result to variable3
	}

	if (variable3 >= 0)													// Print the value of variable #3 if it is positive, otherwise print an error */								
	{	printf("Variable 3:  %d \n", variable3);						// Print the value of variable #3 if it is positive...
	}														
	else																// ...otherwise print an error code.
	{	printf("Something bad happened because variable 3 was not positive. \n");
		printf("Instead, variable 3 turned out to be %d. \n", variable3);
	}

	return 0;
}