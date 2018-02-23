#include<stdio.h>
int main(void)
{
	int a,m,i;
	scanf("%d %d",&a,&m);
	for(i=2;i<=m;i++)
	{
		if(a%i==0 && m%i==0)
		{
			printf("%d",i);
			break;
		}
	}
return 0;
}
