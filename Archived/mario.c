#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>


int main(){
      
      int i;
      int j;
      int input;

      do {
            printf("Enter a height from 1-8: ");
            scanf("%i", &input);
            for ( i = 0; i < input; i++) {
                  for ( j = -1; j < i; j++){
                        printf("#");
                  }printf("\n");
            }
      } while (input < 0 || input > 8);
      return 0; 
}
