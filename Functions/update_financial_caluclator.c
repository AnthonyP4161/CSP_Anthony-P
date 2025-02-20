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
    float type = number/income *100;
}
int main(void){
    inputs("income", &income);
    inputs("rent", &rent);
    inputs("utilities", &utilities);
    inputs("groceries", &groceries);
    inputs("transportation", &transportation);
    return 0;
}