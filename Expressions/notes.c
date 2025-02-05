#include <stdio.h>
#include <math.h>
char name[] = "Anthony";
int num = 12;
float pi = 3.121592653;
float expression = 5*pow(7, 4);
//float equation = 5*7+11/(5-x);
int main(void){
    num = 4;
    printf("%d\n", num);
    printf("%f\n", expression);
    printf("%.999f", pi);
    //printf("%f\n", equation);
    return 0;
}