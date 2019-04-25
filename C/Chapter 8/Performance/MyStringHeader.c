#include <stdio.h>
#include <ctype.h>

#define ERR_NULL_POINTER -1;        // string is null
#define ERR_INVALID_LENGTH -2;      // string length is zero or less

extern int print_the_count(char * inputString, int strLen)
{
    char tempChar = 0;      // Current char being acted on
    int table[26] = {0};    // Alpha
    int count = 0;          // Iterator

    if (!inputString)
    {
        return ERR_NULL_POINTER;        //  Just wrong
    }
    else if (!strLen)
    {
        return ERR_INVALID_LENGTH;      //  You didn't put anything in
    }

    for (int i = 0; i < strLen; i++)
    {
        if (inputString[i] >= 65 && inputString[i] <= 122)  //  Make sure it is a A-z character
        {
            tempChar = inputString[i];      //  tempChar at inputString[i] where i is the index but i is incrementing
            tempChar = toupper(tempChar);   //  make it all YELL AT YOU
            table[tempChar - 65] += 1;      //  iterate through all chars
            count++;
        }
    }

    // Print the table
    for (int i = 0; i < sizeof(table)/sizeof(table[0]); i++)    //  Show how many of each letter
    {
        printf("%c: %d\n", i + 65, table[i]);       // print that table all fancy like
    }
    return count;
}

extern int reverse_it(char * forwardString, int strLen)
{   int i = (0);                //  Iterator
    char tempArray [256]= {0};  //  Empty array
    int reverseI = (strLen);    //  Variable for reverse
    int endI = (reverseI - 1);  //  End of string -1 to forget nul char
    
    if (!forwardString)
    {
        return ERR_NULL_POINTER;        //  Just wrong
    }
    else if (strLen <= 0)
    {
        return ERR_INVALID_LENGTH;      //  You didn't put anything in
    }

    for (i = 0; i < reverseI; i++)
    {   tempArray[i] = forwardString[endI];     //  endI is the index, forwardString is the initial input, tempArray is where you
                                                //  are putting that new string
        endI--;                                 //  Decrement because you're reversing so you're going backwards incrementing
    }

    printf ("\n\tThe reversed string is: %s\n", tempArray);     //  Print that string backwards

    return 0;
    
}