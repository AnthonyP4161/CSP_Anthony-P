#include <stdio.h>
char name[20];
int main(void){
    printf("Type your name: \n");
    scanf("%s", name);
    printf("Your name is: %s", name);
    return 0;
}