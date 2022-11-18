#include <cs50.h>
#include <stdio.h>
#include <math.h>

// Need to round the number to avoid float mistakes. I forget exactly why..
// Need to turn the float into an int for math functions to work smoothly.

// Multiple do while loops to search for 25, 10, 5, and 1 and then
// return a ++ to a coin counter for each one?
float get_user_input(void);

int main(){
    int counter = 0;
    float finput;
    int i;
    finput = get_user_input();
    // printf("This is before math: %f\n", finput);
    float cents = round(finput * 100);
    // printf("This is after math: %f\n", cents);
    // I THINK this just needs to be a while loop with
    // the condition of cents > 25 {cents=cents-25; counter++}
    // do {
    //     cents = cents - 25;
    //     counter++;
    // }while(cents < 25);
    while(cents > 24){
        cents = cents - 25;
        counter ++;
    }
    while (cents > 9){
        cents = cents - 10;
        counter++;
    }
    while (cents > 4){
        cents = cents - 5;
        counter++;
    }
    while(cents > 0){
        cents = cents - 1;
        counter++;
    }
    printf("Total coins: %i\n", counter);
    // printf("cents: %f\n", cents);
    return cents;

}


float get_user_input(){
    float input;
    do{
        input = get_float("Change owed: ");
        // printf("%f\n", input);
    }while(input < 0);
    return input;
}