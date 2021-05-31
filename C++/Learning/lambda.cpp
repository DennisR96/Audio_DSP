/* 
Lambda: 
Methode zum Definieren eines anonymen Funktions Objekts
*/

#include <iostream>

int main(){
    auto lam_add = [] (int x, int y) {return x + y;};                // Addition als Lambda Funktion
    int lam_test = lam_add(12,24);                                   // Lambda Funktion aufrufen
    std::cout << "Lambda Addition: " << lam_test << std::endl;      // Ausgabe

}