#include <stdio.h>
int main()
{
    char b;
    printf("Enter a character: ");
    scanf("%c",&new);

    if( (b>='a' && b<='z') || (b>='A' && b<='Z'))
        printf("%c alphabet.",b);
    else
        printf("%c not an alphabet.",b);

    return 0;
}
