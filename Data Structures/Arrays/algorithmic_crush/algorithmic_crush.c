#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main(void)
{
    int n, m, a, b, k;
    scanf("%d %d", &n, &m);
    
    long *ar, sum = 0, answer = -1;
    ar = (long*)malloc(sizeof(long)*10000000);
    memset(ar, 0, n);
    
    for (int i = 0; i < m; i++)
    {
        scanf("%i %i %i", &a, &b, &k);
        ar[a-1] += k;
        ar[b] -= k;
    }
    
    for (int i = 0; i < n; i++)
    {
        sum += ar[i];
        if (sum > answer)
        answer = sum;
    }
    
    free(ar);
    printf("%ld\n", answer);
    return 0;
}