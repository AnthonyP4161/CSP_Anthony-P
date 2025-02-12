// Anthony Petersen, C Expressions Practice
#include <stdio.h>
#include <math.h>
float equation1 = 7-24/8*4+6;
float equation2 = 18/3-7+2*5;
float equation3 = 6*4/12+72/8-9;
float equation4 = (17-6/2)+4*3;
float equation5 = -2*(1*4-2/2)+(6+2-3);
float equation6 = -1*((3-4*7)/5)-2*24/6;
float equation7 = (3*pow(5,2)/15)-(5-pow(2,2));
float equation8 = (pow(1,4)*pow(2,2)+pow(3,3))-pow(2,5)/4;
float equation9 = pow((22/2-2*5),2) + pow((4-6/6),2);
int main(void){
    printf("%f\n", equation1);
    printf("%f\n", equation2);
    printf("%f\n", equation3);
    printf("%f\n", equation4);
    printf("%f\n", equation5);
    printf("%f\n", equation6);
    printf("%f\n", equation7);
    printf("%f\n", equation8);
    printf("%f\n", equation9);
    return 0;
}