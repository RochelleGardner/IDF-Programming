STRUCT ARRAY INITIALIZATION
##############################################################################################################
/*Initializing After Declaring Structure Array 
*/

struct Book
{
     char bname[20];
     int pages;
     char author[20];
     float price; 
}b1[3] = {
           {"Let us C",700,"YPK",300.00},
           {"Wings of Fire",500,"APJ Abdul Kalam",350.00},
           {"Complete C",1200,"Herbt Schildt",450.00}
         };

/*Explanation:
As soon as after declaration of structure we initialize structure with the pre-defined values. 
For each structure variable we specify set of values in curly braces. 
Suppose we have 3 Array Elements then we have to initialize each array element individually 
and all individual sets are combined to form single set.
*/

{"Let us C",700,"YPK",300.00}

/*
Above set of values are used to initialize first element of the array. 
Similarly –
*/

{"Wings of Fire",500,"APJ Abdul Kalam",350.00}
/*
-is used to initialize second element of the array.
*/
########################################################################################################################
/*Initializing in Main() 
*/
struct Book
    {
     char bname[20];
     int pages;
     char author[20];
     float price; 
};


/* setting up the Book info in the main() function 
*/

void main()
{
struct Book b1[3] = {
        {"Let us Compete",700,"XYZ",300.00},
        {"Wings of Fire",500,"Jane Austen",350.00},
        {"Complete Fire",1200,"Tiffany Moore",450.00}
    };
}