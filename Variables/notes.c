
#include <stdio.h>

char name;
int age = 14;
float pi = 3.14;

int main(void){
    printf("Type your name: \n");
    scanf("%s", name);
    printf("%s\n", name);
    printf("%d\n", age);
    printf("%f\n", pi);
    printf("Hello I am %s. I am %d years old. I like the number %f.", name, age, pi);
return 0;
}