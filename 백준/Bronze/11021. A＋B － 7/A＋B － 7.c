#include <stdio.h>
int main(void)
{
    int T;
    int i;
    int a, b;
    scanf("%d", &T);

    for(i=0; i<T; i++)
    {
        scanf("%d%d", &a, &b);
        printf("Case #%d: %d\n", i+1, a+b);
    }

    return 0;
}