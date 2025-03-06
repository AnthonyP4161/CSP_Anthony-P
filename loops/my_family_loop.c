// Anthony Petersen, My Family Loop
#include <stdio.h>

int main(void){
    char names[][10] = {"Cami", "Alex", "Sierra"};
printf("Hi %s!\n", names);
int nlength = sizeof(names)/sizeof(names[0]);
    return 0;
}