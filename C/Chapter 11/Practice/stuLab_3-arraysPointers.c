/*  Arrays and pointers
    Rochelle Gardner
    21 Feb 2019
    stuLab_3-arraysPointers.c
*/

#include <stdio.h>
#define SIZE 10

void copy1 (char * const s1, const char * const s2);    // prototype
void copy2 (char *s1, const char *s2);                  // prototype

int main (void)
{   char string1 [SIZE];            // create array string1
    char *string2 = "Hello";        // create a pointer to the string
    char string3 [SIZE];            // create array string 3
    char string4 [] = "Good Bye";   // create a pointer to a string
    
    copy1 (string1, string2);
    printf ("string1 = %s\n", string1);
    
    copy2 (string3, string4);
    printf ("string3 = %s\n", string3);

}       // end of main

void copy1 (char * const s1, const char * const s2)     // copy s2 to s1 using array notation
{   size_t i;       // counter
    
    for (i = 0; (s1 [i] = s2 [i]) != '\0'; ++i)         // loop through strings
    {   ;       // do nothing
    }           // end loop
}               // end function copy1

void copy2 (char *s1, const char *s2)       // copy s2 to s1 using pointer notation
{   size_t i;       // counter
    
    for (i = 0; (s1 [i] = s2 [i] ) != '\0'; ++i)
    {   ;       // do nothing
    }           // end loop
}               // end function copy2