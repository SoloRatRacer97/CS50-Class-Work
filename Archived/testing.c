// this includes some boiler plate code, I think
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <math.h>
#include <ctype.h>


// chars = 128, short = 32,000, int = 2,000,0000,000

// Using %8.2f, this says that there are 8 slots for the width of the variable, and that there are 2 decimals that are being shown for the float. * This could be useful later...*
// ==============================================
// Assigning variables and simple math. 
// int main(){
//       // for consts, just make it const in front of the definition of the element. 
//       const float item1 = 5.85;
//       float item2 = 6.85;
//       float item3 = 7.85;

//       printf("Item 1: %8.2f\n", item1);
//       printf("Item 2: %8.2f\n", item2);
//       printf("Item 3: %8.2f\n", item3);
      
//       int x = 9;
//       int y = 2;

//       float z = x % y;

//       printf("%f\n", z);
// }  

// ==============================================
// User inputs and basic strings. 
// int main(){

//       int age;
//       char name[25]; 

//       printf("What is your name?");
      
//       fgets(name, 25, stdin);
//       //This reads the white spaces in a user inuted string. Will be more detail on this later. 
//       name[strlen(name)-1] = '\0';
//       // scanf("%s", name);
//       // printing a new statement
//       printf("How old are you?");
//       // This gets the user input with scan... Although, we are giving it an address for age? This is new...
//       scanf("%d", &age);

//       printf("You are %d years old!\n", age);
//       printf("Your name is %s!", name);
// }

// ==============================================
// Using more adavncted math. INCLUDE: math.h
// int main(){
//       double X = sqrt(9); 
//       double B = pow(2, 4);
//       int C = round(3.14);
//       int D = ceil(5.2);
//       int E = floor(5.2);
//       double F = fabs(-100);
//       double G = log(3);
//       double H = sin(15);
//       double H = cos(15);
//       double H = tan(15);

//       printf("%d", D);
// }


// ==============================================
// Sinple hypotenuse function

// int main(){

//       // declare variables
//       double side1;
//       double side2;
//       double hypotenuse;

//       printf("What is your first side?");
//       scanf("%lf", &side1);
//       printf("What is your second side?");
//       scanf("%lf", &side2);

//       hypotenuse = sqrt(pow(side1, 2) + pow(side2, 2));
//       // need equation
//       printf("Your hypoenuse is equal to %lf", hypotenuse);
//       // Need to send the answer back to the user.
// }
// ==============================================
// If statements
// int main(){
//       int age;

//       // printing the prompt
//       printf("\n Enter your age: ");
//       // Asking user for input and storing it in age. Notice, we still use the & here for the address
//       scanf("%d", &age);

//       if(age >= 18){
//             printf("You are now approved!");
//       }
//       else{
//             printf("You are not old enough!");
//       }
// }

// ==============================================
// Swtich statements
// int main(){
//       char grade;

//       printf("\nEnter in your letter grade: ");
//       scanf("%c", &grade);

//       switch(grade){
//             case 'A':
//                   printf("You got an A, way to go!\n");
//                   break;
//             case 'B':
//             printf("You didnt do too bad\n");
//             break;
//             case 'C':
//             printf("A C, not to shabby!\n");
//             break;
//             case 'D':
//             printf("A D, yikes\n");
//             break;
//             default:
//             printf("Plese enter in your grade!");
//       }
// }

// ==============================================
// Simple Celcius to Ferenhait function. 

// int main(){
//       //Need to ask if the value you have is C or F
//       char label;
//       float degree;

//       printf("Is your temperature in (C) or (F): ");
//       scanf("%c", &label);

//       label = toupper(label);

      

//       if(label == 'C'){
//             printf("What is your temperature: ");
//       scanf("%f", &degree);
//             degree = degree * 100; 
//             printf("Your temperature is %.1f in Ferenhait!", degree);
//       }
//       else if(label == 'F'){
//             printf("What is your temperature: ");
//       scanf("%f", &degree);
//             degree = degree * 11; 
//             printf("Your temperature is %.1f in Ferenhait!", degree);
//       }
//       else{
//             printf("You did not out in the correct values...");
//       }

//       // Need to take in the value of C or F and store it. 

//       // Two if statements... one for each condition. If label is C: if label is F:

//       // print statements after each if function ot show the user their degree. 
// }

// ==============================================
// For loops 
