// you can run debug50 after you make a program that will debug your program

// initiate it with debug50 ./name_of_c_file

#include <stdio.h>
#include <cs50.h>

// int main(void){
//     for(int i=0; i<3; i++){
//         printf("#\n");
//     }
// }
int get_negative_int(void);

int main(void) {
    int i = get_negative_int();
    printf("%i\n", i);
}

int get_negative_int(void){
    int n;
    do {
        n = get_int("Negative Integer: \n");
    } while (n < 0 );
    return n;
}