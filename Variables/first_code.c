#include <stdio.h>
char name[1];
int main(void){
    printf("Type your name: \n");
     scanf("%s", name);
    printf("hello %s\n", name);
    return 0;
}