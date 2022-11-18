#include <stdio.h>
#include <cs50.h>
// Program to determine how many years it will take for a given population
// reach a future population size. 
int main(){
    int start;
    do {
        start = get_int("What is the initial population size? ");
        printf("%i\n", start);
    }
    while (start < 9);
    
    int end;
    do {
        end = get_int("What is the final size of the population? ");

    }
    while (end < start);
    printf("%i\n", end);
    
    // int counter; 
    
    // for ( counter = 0; start < end; counter++) {
    //     float added;
    //     float subtracted;
    //     added = start / 3;
    //     subtracted = start / 4;
    //     start = start + added - subtracted;
    // }
    int counter = 0;
    while (start < end) {
        start = start + (start / 3) - (start / 4);
        counter++;
    }
    printf("Years: %i\n", counter);
}