#include <stdio.h>
#include <cs50.h>

// int main (void){
//     int score1 = 72;
//     int score2 = 73;
//     int score3 = 33;

//     //We CANNOT say that these are floats here since we only computing with ints. So, if we change 3 to 3.0, then we are able to make this into a flaot in the end since all the values within the math will be 'promoted' to a float if operated on by a float.
//     printf("Average: %f\n", (score1 + score2 + score3) / 3.0);

// }

// can also make strings refference variables at certain indexes fo that string.
// ====================================================================
// int main (void)
// {
//     string s = "HI!";
//     printf("%i %i %i\n", s[0], s[1], s[2]);
// }


// Getting the length of a given string: NO NEED! Just use stllen! Sigh....

// ====================================================================
// We can just use strlen here instead....
// int string_length(string s);

// int mian(void){
//     string name = get_string("Name: ");
//     int length = string_length(name);
//     printf("%i\n", length);
// }
// // Gets the length of the string here. Basically just looking at each character and seeing if it is null, or has a value. Then, i gets one added to itself so then at the end, i equlas the length of the string.
// int string_length(string s){
//     int i = 0;
//     while (s[i] != '\0')
//     {
//         i++;
//     }
//     return i;
// }

// ====================================================================
// You can actually store a new variable in a for loop
// int main (void){
//     string s = get_streing("Input: ");
//     printf("Output: ");
//     // See right here....
//     for (int i = 0, n = strlen(s); i++);
//     {
//         printf("%c", s[i]);
//     }
//     pringtf("\n");
// }
// ====================================================================
  