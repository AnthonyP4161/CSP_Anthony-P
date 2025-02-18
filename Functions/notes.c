// Anthony Petersen, C Functions Notes
#include <stdio.h>
int num;
char name[50], place[50], verb[50];
const char* word(char type[50]){
    char choice[50];
    print("Please give a %s", type);
    scanf("%s", choice);
    return choice;
}
int main(void){
    printf("Please tell me a number: \n");
    scanf("%d", num);
    printf("%d", add(int numone+12));
    return 0;
}