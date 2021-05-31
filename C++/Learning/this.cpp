#include <iostream>

class Autos{
    public:
    int x;
    void testing(int x){
        std::cout << "arg(x): \t \t" << x << std::endl;            // Output: Argument (Funktion)
        x = this->x;
        std::cout << "x = this->x: \t" << x << std::endl;            // Output: Klassenvariable
        }
};

int main(){
    Autos Toyota;
    Toyota.x = 5;
    Toyota.testing(2);
}