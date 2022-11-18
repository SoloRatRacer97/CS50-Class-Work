#include <cs50.h>
#include <stdio.h>

int get_user_input(void);

int main (){
    int input = get_user_input();
    int i;
    int j;
    int k;
    int l;
    for (i = 0; i < input; i++){
        for (j = 0; j < 8 - i; j++){
            printf(" ");
        }
        for (k = 0; k <= i; k++){
        printf("#");
        }
        printf(" ");
        
        for (l = 0; l <= i; l++){
            printf("#");
        }printf("\n");
      }
    }
 

int get_user_input (){
    int input;
    do {
        input = get_int("Enter the height: ");
    }while (input > 9 || input < 0);
    return input;
}

// spaces = input - 1; subtracting a space each time
// blocks = 1; adding 1 every time
// adding one space
// adding blocks = 1; adding 1 every time
// NO NEED FOR MORE SPACES