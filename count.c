#include <stdio.h>
int main()
{
    long long num;
    int a = 0;
    printf("integer: ");
    scanf("%lld", &num);
    while(num != 0)
    {
        num /= 10;
        ++a;
    }
    printf("digits: %d", a);
}
