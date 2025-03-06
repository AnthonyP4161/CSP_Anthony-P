//Anthoyn Petersen, loops notes C
#include <stdio.h>

int main(void){
  

    
    

//What is a loop? 
    //loops certain peices of code
//What are the two types of loops?
    //while loops
    int start = 0;
    while(start <5){
        printf("Hello!\n");
        start++;
    }
    

    //for loop
    int q; 
    for(q=0;q<5;q++){
        printf("%d\n", q);
    }
//What is iteration
    // repeating something with minor changes ecery time
//What are arrays(list? 
    // a variable holding multiple values
//How do you make arrays(lists) in C? 
    // array items must all be same data point
int grades[] = {88, 97, 100, 70, 72, 99, 61};
    // 1. set data type 2. AFTER naming put brackets and write the lengthe of the list 3. list must bbe sourounded by curly brackets 4. must use commas between each item of the list
    // print a single item from list
printf("CSP grade: %d\n", grades[2]);
    // change an item
grades[2] = 95;
printf("CSP grade: %d\n", grades[2]);
    //size of list in bytes
int size = sizeof(grades);
 //  in list of items
 int length = sizeof(grades)/(grades[0]);
printf("%d\n", length);

    //array with strings
    //first [] sets length of list
    //second brackets sets length of each string
char movies[][20] = {"Cars", "Treasure Planet", "An American Tale", "Marley and Me", "The Avengers"}; 
printf("The movie is %s\n", movies[1]);
int mlength = sizeof(movies)/sizeof(movies[0]);
//How do you make for loops in C?
    //set the itterator, keeps track of times throiugh the loop (best to set as x or y)
int x;
    // in parenthesis (starting point; ending point; what we count by)
for(x=0;x<=10;x+=2){
    printf("%d\n", x);
}
int m;
for(m=0;m<mlength;m++){
    printf("%s\n", movies[m]);
}

//How do you make while loops in C?
    int w = 0;

    while(w<=100){
        printf("%d\n", w);
        w += 10;
    }


    return 0;
}