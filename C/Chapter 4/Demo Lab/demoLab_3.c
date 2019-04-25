#define _CRT_SECURE_NO_WARNINGS 1            // Disables warning
#include <stdio.h>                           // Standard IO header

int main(void)
{
    char buff[4];                        // Will store string
    printf("Enter string: ");            // Prompts user
    fgets(buff, sizeof(buff), stdin);    // Stores user string
    printf("Your string was: ");         // Prefaces output
    puts(buff);                          // Writes to stdout
    return 0;
    
}
