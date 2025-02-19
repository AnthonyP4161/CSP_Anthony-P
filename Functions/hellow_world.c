// Anthony Petersen, Udate Hello World
#include <stdio.h>
void hello(char name[50]){
    printf("Hello %s", name);
}
int main(void){
    hello("Jack\n");
    hello("John\n");
    hello("Joe\n");
    hello("Jeff\n");
    hello("Jeffrey\n");
    return 0;
}