#include <stdio.h>
int main(){
    char string[100] = "I love you Abiha";
    int i,arr[100],count=0;
    for(i=0;string[i]!='\0';i++){
        arr[i] = string[i];
        count++;
    }
    printf("%d\n",count);
    for(i = 0;i < count;i++){
        printf("%c",arr[i]+10);
    }
    return 0;
}
