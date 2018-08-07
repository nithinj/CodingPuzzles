/*
 * You are given an integer array, where all numbers except for TWO numbers appear even number of times. 
 *
 * Q: Find out the two numbers which appear odd number of times.
 */

#include<stdio.h>
#include<stdlib.h>
int size=0;
int *input;
	

int* testfun(int ch)
{
	if(ch==1)
	{
		size=24;
                static int inp[] = {1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,9,1,2,3,4,1,2,3};
		return inp;
	}
	else if(ch == 2)
	{
		size=24;
                static int inp[] = {1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,9,1,2,3,4,1,2,3};
		return inp;
	}
	else if(ch == 3)
	{
		size=10;
                static int inp[] = {1,2,3,4,2,1,3,6,6,6};
		return inp;
	}
	else if(ch == 4)
	{
		size=18;
                static int inp[] = {1,2,3,4,5,6,7,8,9,10,1,2,4,5,6,7,8,9};
		return inp;
	}
	else
	{
		printf("No test case at this point!\n"); 
		exit(1);
	}
}


int changedbit(int num)
{
	int i;
	for(i = 0; i<sizeof(int)*8; i++)
		if(num & 1<<i)
			return i;
}

main(int argc, char *argv[])
{
	int i=0, xor=0, a=0, b=0;
	if(argc<=1) 
	{
        	printf("You did not feed me arguments, I will die now :( ...");
        	exit(1);
     	}  
	else
	{
		input = testfun(atoi(&argv[1][0]));
		for(;i<size;i++)
			xor^=input[i];
		int pos=changedbit(xor);
		for(i=0;i<size;i++)
			if((input[i] & 1<<pos) == 0)
				a ^= input[i];
			else
				b ^= input[i];
		printf("a: %d, b: %d", a, b);
	}
}
