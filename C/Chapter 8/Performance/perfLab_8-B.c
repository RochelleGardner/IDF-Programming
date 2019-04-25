#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
#include <string.h>
#include "MyStringHeader.h"		// Local header file with quotes

int main()
{
	char userInput[256];		// 256 to avoid a buffer overflow
	char * userString [] = {userInput};		// initialize a new variable to put each character from stdin into the above array

    printf ("\n\tPlease enter a string to be reversed: \n");
    scanf ("%255[^\n]c", &userInput);		// store user input into the array one char at a time
											// 255 field width to protect again from buffer overflow
											// break at \n character

    reverse_it(* userString, strlen(userInput));		// call reverse_it function from MyStringHeader.h
	int counter = print_the_count(* userString, strlen(userInput));	// call print_the_count function from MyStringHeader.h

	printf("\n\n\n\nTotal count: %d\n", counter);		// print that counter

	return 0;
}

