#include<stdio.h>
void main()
{
int h1,m1,h2,m2;
long r,t1,t2;
scanf("%d %d",&h1,&m1);
scanf("%d %d",&h2,&m2);
t1=(h1*60)+m1;
t2=(h2*60)+m2;
if(t1>t2)
{
r=t1-t2;
printf("%ld",r);
}
else
{
r=t2-t1;
printf("%ld",r);
}
}
