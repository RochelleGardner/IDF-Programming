'''
/*  Performance Lab 1: Chapter 4
*   Rochelle Gardner
*   2 Feb 2019
*   perfLab_1
*/

#include <stdio.h>

int main (void)
{
	int userSaid = 0;                                   // initialize vatiable for user input
	printf("Enter a character:  ");                     // prompt user for input
	userSaid = getchar();                               // store the user's input
	printf("The next character sequentially is:  ");    // display
	putchar(userSaid + 1);                              // increment user's character by one

	getchar();

    return 0;
}
'''
#! /usr/bin/env python3

def main():
  ch1 = input("Enter a character: ")
  ch1 = bytes(ch1, 'utf-8') 
  
  s = bytes([ch1[0] + 1]) 
  s = str(s) 

  print ("The next sequential character is: ",s[2]) 
main()