#include<iostream>

int  main(){
int * p ;  // You can only Acess heap by pointer pointing heap memory 
// through stack thus  array is itself address 

// heap memory is treated as resource 


p = new int[5] ; // heap memory is requested to acesss 
//memory allocation 

delete []p; // requested dealloation of memory 
//memory delted 

// if you are not releasing (detelete) . that memory will 
//still belong to your program and you cannot  
// use that particaular memory  because it is already used 
// thus called loss of meory that is meory leak
return  0  ;
}