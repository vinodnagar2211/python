#include <stdio.h>
int main()
{
	int num;
	char ch;
	char value;
	
	printf("Enter value of num and ch :-");
	scanf("%c",&value);
	
	if (value >='A' && value <='Z' || value >='a' && value <='z')
	{
		printf("This is alphabat");
	}
	else 
	{
		printf("This is digit");
	}
	return 0;
}
