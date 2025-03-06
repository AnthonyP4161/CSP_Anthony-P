// Anthony Petersen, My Family Loop
#include <stdio.h>

int main(void){
    char names[][10] = {"Cami", "Alex", "Sierra"};
int nlength = sizeof(names)/sizeof(names[0]);
int n;
for(n=0;n<nlength;n++){
    printf("Hi %s\n", names[n]);
}
    return 0;
}