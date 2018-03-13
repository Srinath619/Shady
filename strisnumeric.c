#include <stdio.h>

int main(void) {
	char n[10];
	scanf("%s",n);
	int i,flag=0;
	for(i=0;n[i]!='\0';i++)
	{
		if(n[i]>='0' && n[i]<='9')
		{
			flag=1;
		}
		else
		{
			flag=0;
			break;
		}
	}
	if(flag==1)
	{
		printf("yes");
	}
	else
	printf("no");
	return 0;
}
