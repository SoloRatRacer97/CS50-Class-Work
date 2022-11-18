#include <cs50.h>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

// American Express 34 and 37
// MasterCard: 51, , 53, 54, 55
// Visa is 4
// probably use switch statements here for the card numbers.

int main (){
    // Initial varaibles to be used:
    int i;
    // Gets user's number
    long card_number;
    card_number = get_long("Please enter your card number: ");
    printf("Your card number is %ld\n", card_number);

    //Gets the length of the user input
    const int nDigits = floor(log10(labs(card_number))) + 1;
    printf("nDigits: %i\n", nDigits);
    // ==============================================================
    // returns the digits into an array. Array that is made is iniatialized
    // with nothing inside of it
    // float digits[nDigits];
    // memset( digits, 0, nDigits*sizeof(digits[0]));
    // printf("Size of the array: %lu\n", sizeof(digits));

    void digitsArray(int myArray[nDigits]) {
        for (int i=0; i<nDigits; i++) {
            printf("%i, ", myarray[i]);
        }
        printf("\n");
    }

    for (i = 0; i < nDigits; i++){
        int digit = card_number % 10;
        printf("Digit = %i\n", digit);
        card_number = card_number / 10;
        printf("Card number = %li\n", card_number);
        int *p = malloc(sizeof(int) * nDigits);
        p[i] = digit;
        printf("Your digits are: %p\n", p);
    }


}


