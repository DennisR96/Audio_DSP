#include <iostream>

class Auto{
    public:
        int x;

};

int main(){
    Auto* Toyota = new Auto;                // Pointer
    Toyota->x = 12;
    std::cout << Toyota->x << std::endl;
    delete Toyota;
    std::cout << Toyota->x << std::endl;
}