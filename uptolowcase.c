#include<stdio.h>
#include<string.h>
int main(void){
	char a[100];
	int l;
	int i;
	scanf("%s",a);
	l=strlen(a);
	for(i=0;i<l;i++){
		if(a[i]>='A'&&s[i]<='Z'){
			a[i]=a[i]+32;
		}
		 else if(a[i]>='a'&&s[i]<='z'){
			a[i]=a[i]-32;
		}
	}
	printf("%s",a);
}
