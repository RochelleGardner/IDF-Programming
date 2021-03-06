/*	Lab 8c: Shadow Sequence Number
		Rochelle Gardner
		15 Feb 2019
		perfLab_8-C.c
*/

#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
#define MAXIMUM_SEQ_NUM (2300) // max number to be calc
#define ERROR_VALUE (105)	

#define MANUAL_TEST
#define AUTO_TEST

unsigned long shadow_sequence_number(int placeNumber); // prototype the function
void clean_stdin(void);

int main(void)
{
	unsigned long tempValue = 0;
	unsigned long myTempValue = 0;
	int i = 0;
	int j = 0;

#ifdef MANUAL_TEST
	int howManyToCalculate = 0;
	tempValue = 0;

	printf("How many numbers would you like to calculate?\n");

	scanf("%d", &howManyToCalculate);


	for (i = 1; i <= howManyToCalculate; i++)
	{
		tempValue = shadow_sequence_number(i);
		printf("%d:\t%lu \n", i, tempValue);
	}
#endif

#ifdef AUTO_TEST

#define BUFF_SIZE 24
	tempValue = 0;
	int numberOfTestsRun = 0;
	int numberOfTestsPassed = 0;

	int placeNumbers[BUFF_SIZE] = { -31337, ((MAXIMUM_SEQ_NUM + 1) * -1), (MAXIMUM_SEQ_NUM * -1), -1337, -100,
	0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 100, 1337, MAXIMUM_SEQ_NUM, (MAXIMUM_SEQ_NUM + 1), 31337 };

	unsigned long returnValues[BUFF_SIZE] = { ERROR_VALUE, ERROR_VALUE, ERROR_VALUE, ERROR_VALUE, ERROR_VALUE,
	ERROR_VALUE, 9, 0, 9, 25, 50, 86, 135, 199, 280, 380, 501, 645, 814, 338345, 797553920, 4058312045, ERROR_VALUE, ERROR_VALUE };

	for (i = 0; i < BUFF_SIZE; i++)
	{
		tempValue = shadow_sequence_number(placeNumbers[i]);
		numberOfTestsRun++;
		if (tempValue == returnValues[i])
		{
			numberOfTestsPassed++;
		}
	}

	printf("\n\nNumber of tests run:\t%d\n", numberOfTestsRun);
	printf("Number of tests passed:\t%d\n", numberOfTestsPassed);
#endif

	return 0;
}


/*
 * This pre-processing directive determines whether the program will
 *     run unit tests and/or prompt the user for input depending on
 *     what #define statements are uncommented.
#define MANUAL_TEST // Allows the programmer to manually provide input to test the response of the program as a whole
#define AUTO_TEST // Runs unit tests on unsigned long shadow_sequence_number(int placeNumber)
 * Uncomment out multiple #defines to multiple tests in a single run
 */


void clean_stdin(void)
{   int c;
    do {
        c = getchar();
    } while (c != '\n' && c != EOF);
}

unsigned long shadow_sequence_number(int placeNumber)
{   int returnThis;
    
    if ((placeNumber < 0) || (placeNumber > 2300))      // if the number is negative or greater than 2300; error
    {   returnThis = 105;
    }
    else if (placeNumber == 1)      // First is always 9
    {   returnThis = 9;
    }
    else if (placeNumber == 2)      // Second is always 0
    {   returnThis = 0;
    }
    else 
    {   returnThis = (shadow_sequence_number(placeNumber -1 ) + (placeNumber * placeNumber));     // S(n) = S(n -1) + (n * n)
    }
    return returnThis;
}

/*
The Shadow Sequence:
    Starts with 9 and 0 then each subsequent number is calculated by adding the previous value and the square of the position
    S(n) = S(n-1) + (n*n)
*/

/*
 * FUNCTION:   unsigned long shadow_sequence_number(int placeNumber)
 *
 * ARGUMENTS:  placeNumber represents the individual "Shadow Sequence" position number to calculate
 *
 * RETURNS:	   The value of of the "Shadow Sequence" number at position "placeNumber" [see: S(placeNumber)].
 *			   The "Shadow Sequence" is calculated utlizing the following algorithm:
 *                 S(n) = S(n-1) + (n * n) where "n" represents a given position and S(n) represents the value at
 *                     position "n".  S(1) is always equal to 9.  S(2) is always equal to 0.  The algorithm begins
 *                     calculating at S(3).  (see NOTES: for details)  
 *             ERROR_VALUE (105) if placeNumber is unrealistic or dangerous
 *
 * NOTES:      This function should only be returning a single sequence number from the "Shadow Sequence".
 *             This function should *not* be calculating multiple sequence numbers during a single function call.
 *             Nor should this function be printing any sequence numbers.
 *             However, this function will need to call itself recursively to calculate all of the previous sequence
 *                 numbers in order to calculate the sequence number at position "placeNumber".
 *             Any requirements to calcualte or print multiple numbers in the "Shadow Sequence" should be
 *                 accomplished by the calling function [e.g., main()]
 *             The data type of long was chosen as the return value to increase the available output.
 *             The keyword unsigned was chosen to further maximize the available output since this algorithm
 *                 should not be producing any negative numbers.
 *			   The "Shadow Sequence" is calculated utlizing the following algorithm:
 *                 S(n) = S(n-1) + (n * n) where "n" represents a given position and S(n) represents the value at
 *                     position "n".  S(1) is always equal to 9.  S(2) is always equal to 0.  The algorithm begins
 *                     calculating at S(3).  For example, here are some sample calculations of S(n)
 *                     S(1) = 9.
 *                     S(2) = 0.
 *                     S(3) = S(2) + (3 * 3) ---> S(3) = (0)  + (9) ---> S(3) = 9.
 *                     S(4) = S(3) + (4 * 4) ---> S(4) = (9)  + (16) --> S(4) = 25.
 *                     S(5) = S(4) + (5 * 5) ---> S(5) = (25) + (25) --> S(5) = 50.
 *
 *             The first few "Shadow Sequence" numbers are as follows:
 *                 S(1)		S(2)	S(3)	S(4)	S(5)	S(6)	S(7)	S(8)	S(9)	S(10)
 *                 9		0		9		25		50		86		135		199		280		380
 */
