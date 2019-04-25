ines (12 sloc)  463 Bytes
#include <stdio.h>
/*		PART ONE
Read a first, middle and last name as input into separate char arrays
Specify a field-width to protect against buffer overflow
Ensure the field-width leaves room for a nul-terminator
Specify a ("\t") as a delimitating character
Print the full name, separating each string with a tab and newline ("\t\n")
*/

int main(void)
{
	char testCase[] = {'A', 'B', 'C', '\0'};
	double currentTemp[] = {100.1234, 99.876543, 133.7};
	int numOfRuns[] = {3, 4, 5};
	
	printf("%-12Test Case %-12Temp(F) %12-# of Runs\n");
	printf("%-12c %-012.2f %-12d\n", testCase[0], currentTemp[0], numOfRuns[0]);
	printf("%-12c %-012.2f %-12d\n", testCase[1], currentTemp[1], numOfRuns[1]);
	printf("%-12c %-012.2f %-12d\n", testCase[2], currentTemp[2], numOfRuns[2]);
	return 0;
}

/*		PART TWO
Read two integers from one line
Format the input so that the integers are separated by an asterisk (*) x*y (e.g., 2*3, 11*14)
Reprint the two integers and result as if the answer were being read by a human
////////////// EXAMPLE #1 ///////////////
OUTPUT:  Enter two integers, separated by a *, to be multiplied…
INPUT:   2*3
OUTPUT:  The result of 2 multiplied by 3 is 6.  
////////////// EXAMPLE #2 ///////////////
OUTPUT:  Enter two integers, separated by a *, to be multiplied…
INPUT:   11*14
OUTPUT:  The result of 11 multiplied by 14 is 154.
*/