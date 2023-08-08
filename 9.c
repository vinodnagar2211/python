#include <stdio.h>
int main()
{
	int a,b,c;
	printf("Enter Value of a and b :-");
	scanf("%d %d d",&a,&b,&c);
	
	if (a>b && a>c)
	{
		printf(" A is grether then");
	}
	else if (b>a && b>c)
	{
		printf(" B is grether then");
	}
	else if (c>a && c>b)
	{
		printf(" C is grether then");
	}
	else 
	{
		printf(" NUm is Equal Equal");
	}
	
	return 0;
}
