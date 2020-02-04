#include <stdio.h>

int main() {
    
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int i, j;
    int n, d;
    int array[100002];
    int temp;
    scanf("%d %d\n", &n, &d);
    
    for(i=0;i<n;i++)
        scanf("%d", &array[(n-d+i)%n]);
    
    for(i=0;i<n;i++)
        printf("%d ", array[i]);
    
    return 0;
}