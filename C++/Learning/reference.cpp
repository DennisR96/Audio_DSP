// References
#include <iostream>

void work(int &x){
    // &x --> Kopiert den Datensatz nicht extra für die Funktion
    x = x + 1;
}

void swap(int &x, int &y){
    // Tauscht den Speicherplatz zweier Variableny
    int temp = y;
    y = x;
    x = temp;
}

int main(){
    int a = 5;                          // Variable
    int &b = a;                         // Reference    (same = int&b)
    std::cout << "Variable: " << a << std::endl;
    std::cout << "Referenz: " << b << std::endl;
    std::cout << "Adresse a: " << &a << " Adresse b: " << &b << std::endl;

    // Referenzen in Funktion ändern
    work(a);
    std::cout << std::endl;
    std::cout << "Referenz in Funktion ändern" << std::endl;
    std::cout << "A durch Funktion: " << a << std::endl;

    // Swap Funktion
    std::cout << std::endl; 
    std::cout << "Funktion: Speicher Tauschen" << std::endl;
    int x = 3;
    int y = 4;
    swap(x,y);
    std::cout << "x: " << x << std::endl;
    std::cout << "y: " << y << std::endl;

}