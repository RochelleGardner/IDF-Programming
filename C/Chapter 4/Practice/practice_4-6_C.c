#include <stdio.h>

int main(void) 
{
    float aNum = 12.3456;

    printf ("%f \n ", aNum);
    printf ("%f \n ", aNum * -1.0);
    printf ("%+f \n ", aNum);
    printf ("%+f \n ", aNum * -1.0);
    printf ("% f \n ", aNum);
    printf ("% f \n ", aNum * -1.0);
    printf ("%-f \n ", aNum);
    printf ("%-f \n ", aNum * -1.0);
    printf ("%0f \n ", aNum);
    printf ("%16f \n ", aNum);

    return 0;
    
}