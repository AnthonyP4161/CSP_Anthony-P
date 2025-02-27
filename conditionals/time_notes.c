// Anthony Petersen, Time Of Day
#include <stdio.h>
#include <time.h>


int main(void){
    time_t seconds; //time since January 1st 1970
    seconds = time(NULL);
    //printf("Time since January 1st 1970 in seconds\n=\n%d \n", seconds);

    //current time
    time_t rawtime;
    struct tm * timeinfo;
    time(&rawtime);
    timeinfo = localtime(&rawtime);
    //printf("Our current time and date is %s \n", asctime(timeinfo));

    //current hour
    time_t now = time(NULL);
    struct tm * tm_struct = localtime(&now);
    int hour = tm_struct->tm_hour;
    printf("%d", hour);
    return 0;
}