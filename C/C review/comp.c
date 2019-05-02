#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

/*
int pattern function
    while not EOF
        do the pattern matching (need more research and maybe help but not yet)
    
    return patterns
*/

int main()
{   FILE *fp = NULL;    
    char ch,f[100],c,d;

    printf ("Enter the file name: \n");
    scanf("%s", f);

    fp = fopen(f,"r");  // open the file to read

    if (!fp)    // error handling
    {   printf("Cannot open file!\n");
        exit(-1);   // quit
    }
    
    do
    {   ch = fgetc (fp);    // get the chars from the file
        /*
            for each char
                count the occurences

            if the count on a char is more than 3
                replace with something
            if the count on a char is more than 2
                replace with something else
            else 
                call the pattern searcher
            print the new text
        */
        
    } while (ch != EOF);    // while there's still file left do ^
    //write the new text to the file
    fclose(fp); // always close the file
   
}