// Anthony Petersen, FizzBuzz
#include <stdio.h>
int number = 1;


int main(void){
    while(number <= 50){
        if(number%3==0 && number%5==0){
            printf("FizzBuzz\n");
        }else if(number%5==0){
            printf("Buzz\n");
        }else if(number%3==0){
            printf("Fizz\n");
        }else{
            printf("%d\n", number);
        }
            number += 1;
        }

return 0;
}