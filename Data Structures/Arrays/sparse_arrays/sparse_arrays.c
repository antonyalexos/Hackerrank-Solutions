#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int Q,N,i,j,sum;
    char string[1000][20],queries[1000][20];
    
    scanf("%d",&N);
    for(i=0;i<N;i++)
        scanf("%s",string[i]);
    scanf("%d",&Q);
    
    for(i=0;i<Q;i++){
        scanf("%s",queries[i]);
        for(j=0;j<N;j++){
            if(strcmp(queries[i],string[j])==0)
                sum+=1;
        }
        printf("%d\n",sum);
        sum = 0;
    }
    return 0;
}