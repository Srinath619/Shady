#include<stdio.h>
#include<string.h>
int main(void){
	char s[100];
	char v[100];
	int k=0;
	int m=1;
	int j;
	int a[26]={0};
	int b[26]={0};
	scanf("%s",s);
	scanf("%s",v);
	while(s[k]!='\0'){
		a[s[k]-'a']++;
		k++;
		
	}
	k=0;
	while(v[k]!='\0'){
		b[v[k]-'a']++;
		k++;
		
	}
	for( j=0;j<26;j++){
		if(a[j]!=b[j]){
			m=0;
			break;
		}
	}
	if(m==0){
		printf("not equal");
	}
	else{
		printf("equal");
	}
	
}
