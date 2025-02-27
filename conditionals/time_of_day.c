// Anthony Petersen, Template
#include <stdio.h>
#include <time.h>



int main(void){
    time_t now = time(NULL);
    struct tm * tm_struct = localtime(&now);
    int hour = tm_struct->tm_hour;
    if(hour >= 17){
        printf("Good evening! \n");
    }else if(hour >= 12){
        printf("Good afternoon! \n");
    }else
        printf("Good morning!");
    return 0;
}