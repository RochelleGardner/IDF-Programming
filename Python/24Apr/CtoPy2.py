'''
/*      Performance Lab 5A
*           Rochelle Gardner
*           6 Feb 2019
*           perfLab_5-a.c
*       Write a program to calculate the hypotenuse of a right triangle
*       using Pythagorean's Theorem.
*       Input the two legs (A and B)- Output the hypotenuse (C)
*/

#include <stdio.h>
#include <math.h>

int main (void)
{
    int sideA = 0;
    int sideB = 0;
    double sideC = 0;

    printf ("Enter the length of side A as a whole number: ");          // Prompt the user for sideA length
    scanf ("%64i", &sideA);                                             // Store the input into the sideA variable
    printf ("Enter the length of side B as a whole number: ");          // Prompt the user for sideB length
    scanf ("%64i", &sideB);                                             // Store the input into the sideB variabl
    if ((sideA > 0) && (sideB > 0))
    {
        sideC = ((sideA * sideA)  + (sideB * sideB));
        printf ("The hypotenuse is %lf", (sqrt(sideC)));
    }                            
    else
    {
        printf ("Please put in values greater than 0.");
    }
    return 0;
};
'''
#! /usr/bin/env python3

def main():
    sideA = int(input("Enter the length of side A: "))
    sideB = int(input("Enter the length of side B: "))
    if (sideA > 0) and (sideB > 0):
        sideC = ((sideA * sideA)  + (sideB * sideB))**0.5
        print("The hypotenuse is ", sideC)
    else:
        print("Please put in values greater than 0...")
        main()
    
main()