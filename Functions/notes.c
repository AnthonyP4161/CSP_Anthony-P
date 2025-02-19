// Anthony Petersen, C Functions Notes
#include <stdio.h>
int num;
//char name[50], place[50], verb[50];
//const char* word(char type[50]){
   // char choice[50];
    //print("Please give a %s", type);
    //scanf("%s", choice);
    //return choice;
    
//}
void due(char assignment[50], char day[20]){
    printf("The %s assignment is due %s", assignment, day);

}
int main(void){
    //printf("Please tell me a number: \n");
    //scanf("%d", num);
    //printf("%d", add(int numone+12));
    due("functions notes", "today\n");
    due("Hello world update", "tommorow\n");
    due("Financial calculator update", "Friday\n");
    return 0;
}