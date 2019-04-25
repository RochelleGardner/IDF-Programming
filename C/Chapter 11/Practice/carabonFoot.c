
// Making a Difference: Carbon Footprint Calculator
#include <stdio.h>

// prototypes
void getCarbonFootPrintCar( void );
void getCarbonFootPrintBuilding( void );
void getCarbonFootPrintBike( void );

// function main begins program execution
int main ( void )
{
   int choice; // variable to hold user's choice

   // initialize array of 3 pointers to functions that each take
   // a void argument and return void
   void(*f[3])(void) = { getCarbonFootPrintCar, 
      getCarbonFootPrintBuilding, getCarbonFootPrintBike };

   puts( "Welcome to the Carbon Footprint Calculator.\n"
      "Please input the following information "
      "to calculate the carbon footprints\n"
      "of a car, building, and bike.");

   printf( "%s", "\nEnter 0 to calculate the carbon footprint of a car\n"
      "1 to calculate the carbon footprint of a building\n"
      "2 to calculate the carbon footprint of a bike\n"
      "3 to end: ");
   scanf( "%d", &choice );

   // process user's choice
   while (choice >= 0 && choice < 3) {
      // invoke function at location choice in array f and pass
      // choice as an argument
      (*f[choice])();
      
      printf( "%s", "\n\nEnter 0 to calculate the carbon footprint of a car\n"
      "1 to calculate the carbon footprint of a building\n"
      "2 to calculate the carbon footprint of a bike\n"
      "3 to end: " );
      scanf("%d", &choice);
   }// end while

   puts( "Thank you for using the carbon footprint calculator" );
} // end main

// calculates the carbon footprint of a car
// one gallon of gas yields 20 pounds of CO2 
// http://www.enviroduck.com/carbon_footprint_calculations.php
void getCarbonFootPrintCar(void)
{
   float gallons;
   // get number of gallons in car
   printf( "%s", "Please input the number of gallons used: " );
   scanf( "%f", &gallons );
   
   printf( "The carbon footprint of a car that used %.2f gallons is %.2f.\n",
      gallons, 20*gallons);
} // end getCarbonFootPrintCar 

// calculates the carbon footprint of a building 
// simplified formula: multiply the square footage by 50 
// for the wood frame, by 20 for the basement,
// by 47 for the concrete, and 17 for the steel
// http://www.greenerpath.org/Building_Carbon_Footprint.html
void getCarbonFootPrintBuilding(void)
{
   float squareFootage;
   // get square footage in building
   printf( "%s", "Please input the square footage of a building: " );
   scanf( "%f", &squareFootage);
   
   printf( "The carbon footprint of a building with %.2f square feet is %.2f.\n", 
      squareFootage, 50 * squareFootage + 20 * squareFootage +
      47 * squareFootage + 17 * squareFootage);
} // end getCarbonFootPrintBuilding

// Not counting the carbon used to make the bicycle, 
// a bike's carbon footprint is 0.
// http://www.livemint.com/2009/06/04230851/How-big-is-your-carbon-footpri.html?pg=1
void getCarbonFootPrintBike(void)
{
   printf( "The carbon footprint of a bike is %.2f.\n", 0 );
} // end getCarbonFootPrintBike3
