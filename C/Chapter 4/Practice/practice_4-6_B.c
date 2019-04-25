#include <stdio.h>

int main(void) 
{
    char myStr [] = {"Hello world!"};

    printf ("%s \n ", myStr);
    printf ("%0s \n ", myStr);
    printf ("%2s \n ", myStr);
    printf ("%4s \n ", myStr);
    printf ("%8s \n ", myStr);
    printf ("%16s \n ", myStr);
    printf ("%25s \n ", myStr);

    return 0;
    
}