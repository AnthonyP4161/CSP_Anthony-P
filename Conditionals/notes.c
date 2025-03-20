// Anthony Petersen, Template
#include <stdio.h>
#include <string.h>
char name[]= "Bob";
int num;
int main(void){
    //How do you write an if statement in C?
    if(strcmp(name, "Anthony") == 0){;
        printf("Hello Anthony, welcome to class. \n");
    //How do you write else statements in C?
    }else{
        printf("Hello %s, welcome to class. \n", name);
    }
    printf("How many siblings do you have: \n");
    scanf("%d", &num);
    //How do you write elif/ else if statements in C?
    if(num == 0){
        printf("You have no siblings, skill issue \n");
    }else if(num <= 2){
        printf("You have a couple siblings \n");
    }else if(num <= 5){
        printf("You have a few siblings \n");
    }else{
        printf("You have too many siblings little bro \n");
    }
    //How do you write the 3 logical operators in C?
    // && = and
    // || = or
    // ! = not
    if(num == 7 || num == 13){
        printf("Oh golly gee that's an unlucky number \n");
    }else if(num < 10 && num > 5){
        printf("%d is a large single digit number \n", num);
    }else if(!(num > 10)){
        if(num == 12){
            printf("That is in fact a dozen. \n");
        }else{
            printf("Your number is less than 10 \n");
        }
    }else{
        printf("You, unknowingly, typed in %d \n", num);
    }
    return 0;
}



