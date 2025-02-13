// Anthony Petersen, Template
#include <stdio.h>
#include <string.h>
    char name[100];
int main(void){
    char decoration1[100] = "(O_O)";
    char decoration2[100] = "(O_O)";
    printf("Hello, what is your name: \n");
     scanf("%s", name);
    strcat(decoration1, name);
    strcat(decoration1, decoration2);
    printf("%s\n", decoration1);
return 0;
}