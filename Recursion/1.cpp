// A Function calling itself called recursion 
// and inside recursion their their should be the condition code by which it should stop 

// simple exmaple

//accending order 
#include<iostream>
using std::cout ;
using std::cin ; 
using std :: end ; 



void func1(int n){
    if (n>0){
        cout<<(n);
        return func1(n - 1 );
}

}


int main(){
    int n = 4 ; 
    func1(n);

}