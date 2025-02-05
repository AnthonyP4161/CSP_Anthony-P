#include <stdio.h>
char name;
int main(void){
    printf("Type your name: ");
    scanf("%s", &name);
    printf("Your name is: %s", name);
    return 0;
}