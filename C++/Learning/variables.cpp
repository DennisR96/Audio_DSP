// -    -   -   Variables   -   -   -
#include <iostream>
#include <string>

bool boole = true;
char character = 'A';
const int konstante = 24;
double doppel = 12.345678;
float floating = 12.345678;
int integer = 123;

std::string text = "Das ist ein Text";

int main(){
    std::cout << std::boolalpha <<" --- Variables ---" << std::endl;
    std::cout << "Boolean: \t" << boole << std::endl;
    std::cout << "Character: \t" << character << std::endl;
    std::cout << "Constant: \t" << konstante << std::endl;
    std::cout << "Double: \t" << doppel << std::endl;
    std::cout << "Float: \t \t" << floating << std::endl;
    std::cout << "Integer: \t" << integer << std::endl;
    std::cout << "String: \t" << text << std::endl;
    

    return 0;
}

