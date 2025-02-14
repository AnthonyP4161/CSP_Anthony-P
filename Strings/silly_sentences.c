// Anthony Petersen, C Silly Sentences
#include <stdio.h>
//empty string variables for user words (minimum 3)
char adjective[100];
char noun[100];
char name[100];
char place[100]; 
int main(void){
    //welcom user and explain program
printf("Welcome to Silly Sentences. This program functions like a mad lib, but it's digital \n");
    //ask user for words(only one word, not multi word answers)
    printf("Please enter a noun: \n");
    scanf("%s", noun);
    printf("Please enter an adjective: \n");
    scanf("%s", adjective);
    printf("Please enter a name: \n");
    scanf("%s", name);
    printf("Please enter the name of a city: \n");
    scanf("%s", place);
    //print the silly goofy story
    printf("%s went to %s, so he could get a %s %s \n", name, place, adjective, noun);
    return 0;
}