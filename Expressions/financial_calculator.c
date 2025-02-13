// Anthony Petersen, Financial Calculator
#include <stdio.h>
#include <math.h>

float income;
float rent;
float utilities;
float groceries;
float transportation;

int main(void){
//welcome user and explains programs use
    printf("Welcome to your financial calculator, which will calculate your expenses, savings, and spending money \n");
//have user input monthly income
    printf("How much is your monthly income: ");
    scanf("%f", &income);
//have user input cost of rent
    printf("How much is your monthly rent cost: ");
    scanf("%f", &rent);
//have user input cost of utilities
    printf("How much is your monthly utilities cost: ");
    scanf("%f", &utilities);
//have user input cost of groceries
    printf("How much is your monthly groceries cost: ");
    scanf("%f", &groceries);
//have user input cost of transportation
    printf("How much is your monthly transportation cost: ");
    scanf("%f", &transportation);
    //calculate percent of income used for savings
    float savings = (income)*.1;
//calculate percent of income used for rent (rent/income *100)
    float percent_rent = (rent / income) * 100;
//calculate percent of income used for utilities (utilities/income *100)
    float percent_utilities = (utilities / income) * 100;
//calculate percent of income used for groceries (groceries/income *100)
    float percent_groceries = (groceries / income) * 100;
//calculate percent of income used for transportation (transportation/income *100)
    float percent_transportation = (transportation / income) * 100;
//calculate percent of income used for savings (savings/income *100)
    float percent_savings = (savings / income) * 100;
//calculate how much is spending(income minus savings and expenses)
    float spending = income-(rent+utilities+groceries+transportation+savings);
//calculate percent of income used for spending
    float percent_spending = (spending/income)* 100;
//printf the following

    //your rent is $ which is % of your income
    printf("Your rent costs $%.2f, which is %.0f percent of your income \n", rent, percent_rent);
    //your utilities is $ which is % of your income
    printf("Your utilites cost $%.2f, which is %.0f percent of your income \n", utilities, percent_utilities);
    //your groceries is $ which is % of your income
    printf("Your groceries cost $%.2f, which is %.0f percent of your income \n", groceries, percent_groceries);
    //your transportation is $ which is % of your income
    printf("Your transportation costs $%.2f, which is %.0f percent of your income \n", transportation, percent_transportation);
    //your savings is $ which is % of your income
    printf("You're saving $%.2f, which is %.0f percent of your income \n", savings, percent_savings);
    //your spending is $ which is % of your income
    printf("Your spending money is $%.2f, which is %.0f percent of your income \n", spending, percent_spending);
    return 0;
}