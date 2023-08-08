//              Leap Year code

#include <stdio.h>

int main()
{
    int year;
    printf("Enter The Year :-");
    scanf ("%d",&year);
    
    if (year%4==0  && year % 400==0)
    {
        printf("The is Leap Year");
    }
    else
    {
        printf("This in Not Leap Year");
    }

    return 0;
}

