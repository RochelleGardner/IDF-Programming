#include <stdio.h>

#define firstStr "Test 1"
#define secondStr " works!"
#define bothStr firstStr secondStr
#define constBUFF 64

int main(void)
{/*  Chapter 10 Lab 10.6 A
    Rochelle Gardner
    20 Feb 2019
    perfLab_10-6A.c
    
    Write a C program with:
        1. Combine two string literals
        2. Wrap those in quores
        3. Defiine const buffer of 64
    Define Array:
        1. of standard buff
        2. assign the wrapped string literals
*/

#include <stdio.h>

#define firstStr "Test 2384761"		// make the first string literal
#define secondStr " works!"			// make the second string literal
#define bothStr firstStr secondStr	// put 'em together
#define constBUFF 64				// make sure you don't get an overflow

int main(void)
{
	char myArray[constBUFF] = bothStr;	// array with buff size and set to wrapped strings
	printf (myArray, constBUFF);		// display that stuff

	return 0;
}