#include <stdio.h>

#define firstStr "Test 2384761"
#define secondStr " works!"
#define bothStr firstStr secondStr
#define constBUFF 64

int main(void)
{
	char myArray[constBUFF] = bothStr;
	printf (myArray, constBUFF);

	return 0;
}