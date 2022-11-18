 #include <cs50.h>
 #include <stdio.h>

 int main(void)
 {
   // Getting a number from the user.
   // get is how you interact with the user in C
   long x = get_long("x: ");

   long y = get_long("y: ");

   // This says print a number, and make a new
   // line. Then, we pass the x+y to it so it adds
   printf("%li\n", x+y);
}