#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Gets the inputs from the user
    int x = get_int("x: ");
    int y = get_int("y: ");
    
    // does zeh math.
    float z = (float) x / (float) y;
    
    // Prints the statement, %f\n
    printf("%f\n", z);
}