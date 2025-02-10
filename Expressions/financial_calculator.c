// Anthony Petersen, Financial Calculator
#include <stdio.h>

int income;
float rent;
float utilities;
float groceries;
float transportation;

int main(void){
//welcome user and explains programs use
    printf("Welcome to your financial calculator, which will calculate your expenses, savings, and spending money \n");
//have user input monthly income
    printf("How much is your monthly income: ");
    scanf("%d", &income);
//have user input cost of rent
    printf("How much is your monthly rent cost: ");
    scanf("%d", &rent);
//have user input cost of utilities
    printf("How much is your monthly utilities cost: ");
    scanf("%d", &utilities);
//have user input cost of groceries
    printf("How much is your monthly groceries cost: ");
    scanf("%d", &groceries);
//have user input cost of transportation
    printf("How much is your monthly transportation cost: ");
    scanf("%d", &transportation);
//calculate percent of income used for rent (rent/income *100)

//calculate percent of income used for utilities (utilities/income *100)

//calculate percent of income used for groceries (groceries/income *100)

//calculate percent of income used for transportation (transportation/income *100)

//calculate percent of income used for savings (savings/income *100)

//calculate how much is spending(income minus savings and expenses)

//printf the following

    //your rent is $ which is % of your income

    //your utilities is $ which is % of your income

    //your groceries is $ which is % of your income

    //your transportation is $ which is % of your income

    //your savings is $ which is % of your income
    
    //your spending is $ which is % of your income
    return 0;
}