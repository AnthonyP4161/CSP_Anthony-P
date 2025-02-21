// Anthony Petersen, Update Financial Calculator
#include <stdio.h>
#include <math.h>

float income;
float rent;
float utilities;
float groceries;
float transportation;

void inputs(char type[50], float *input){
    printf("How much is your monthly %s in a dollar amount: \n", type);
    scanf("%f", input);
    return;
}
void percentage(char type[50], float *number){
    float percent = *number/income *100;
    printf("Your %s is $%.2f which is %.1f%% of your income \n", type, *number, percent);
    return;
}
int main(void){
    inputs("income", &income);
    inputs("rent", &rent);
    inputs("utilities", &utilities);
    inputs("groceries", &groceries);
    inputs("transportation", &transportation);
    percentage("rent", &rent);
    percentage("utilities", &utilities);
    percentage("groceries", &groceries);
    percentage("transportation", &transportation);
    float savings = income*.1;
    float spending = income-rent-utilities-groceries-transportation-savings;
    printf("Your savings is $%.2f which is 10%% of your income.\n", savings);  
    printf("Your spending monet left over is $%.2f.\n", spending);  

    return 0;
}