#include <iostream>
using std::cout ;

void fun(int n){
    if (n > 4 ){

        //calling fucntion ahead of print statement 
        fun(n - 1 ) ; 
        cout<<n;
    } 

}
int  main(){

    int n = 4 ;
    fun(n);


}

