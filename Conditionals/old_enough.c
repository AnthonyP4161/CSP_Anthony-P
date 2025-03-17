// Anthony Petersen, Old Enough
#include <stdio.h>
int age;
int main(void){
    printf("How old are you in years: \n");
    scanf("%d", &age);
    if(age >= 18){
    printf("You can vote! \n");
    }else if(age >= 16){
        printf("You can get a drivers license! \n");
    }else if(age == 15){
        printf("You can get a learners permit! \n");
    }else if(age >= 4){
        printf("You can go to school! \n");
    }else{
        printf("You are a newborn, how are you even typing? \n");
    }

    return 0;
}