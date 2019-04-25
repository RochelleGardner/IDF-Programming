/*  
*       Performance Lab 3: Chapter 4
*       Rochelle Gardner
*       2 Feb 2019
*       perfLab_4-C
*/

#include <stdio.h>

int main (void)
{
    char buff[10];
	printf("Enter a string:     ");
	fgets(buff, sizeof(buff), stdin);
	printf("Your string was:    ");
	fputs(buff, stdout);

    return 0;
}    