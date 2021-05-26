#include <iostream>
#include <vector>

void print_vector(std::vector<int> x){
    std::cout << "Vector: x = {";
    for (std::vector<int>::iterator i = x.begin(); i != x.end(); ++i)
        std::cout << *i << ',';
    int end = x.size();
    std::cout << "} " << std::endl;
}
 
int main()
{
    // 1. Create Vector -> std::vector<type> <name> (n, val)
    // Index: x[0,1,2,3,4] 
    std::vector<int> x;
    
    // Operate on a Vector
    x.push_back(1);                      // Add Variable to the End                
    x.push_back(2);
    x.push_back(3);
    x.push_back(4);
    
    x.pop_back();                         // Pop last Variable
    
    //x.clear();                            // Clear Vector  
    
    // Ausgabe Eigenschaften
    std::cout << "-- Vektoreigenschaften -- " << std::endl;
    print_vector(x);  
    int n = 1;   
    std::cout << "Element: x[" << n << "]" << "-> " <<x[n] << std::endl;                                        
    std::cout << "Größe: " << x.size() << std::endl;
    
}