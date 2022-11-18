#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include <cs50.h>
// This make a pyramid of "mario blocks" given a user input. Takes in some
// design constraints. 
int get_user_input(void);

int main(){
    // i = the input
    int input = get_user_input();
    int i;
    int j;
    int k;
    int l;
    // i = HEIGHT
    for ( i = 0; i < input; i++) {
                    // j = LENGTH
                    // for ( j = 0; j <= i; j++){
                        // k = spaces
                        for (k = 0; k < 8 - i; k++){
                                printf(" ");
                        }
                        // l = number of #s
                        for(l = 0; l <= i; l++){
                        printf("#");
                        }printf("\n");
                    // }printf("\n");
    }
}

int get_user_input (){
    int n;
    do {
        n = get_int("Input a value between 1-8: ");
    }
    while(n < 1 || n > 8);
    return n;
}
