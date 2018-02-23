#include <stdio.h>
#include<string.h>
int main(void) {
	char s[10],a;
	int i,l;
	scanf("%[^\n]s",s);
	l=strlen(s);
	if(l%2==0)
	{
	for(i=0;i<l;i+=2)
             {
             a=s[i];
             s[i]=s[i+1];
             s[i+1]=a;
             }
   	 printf("%s",s);
	}
    else
    {
    for(i=0;i<l;i+=3)
             {
             a=s[i];
             s[i]=s[i+1];
             s[i+1]=a;
             }
   	 printf("%s",s);
	}
	return 0;
}
