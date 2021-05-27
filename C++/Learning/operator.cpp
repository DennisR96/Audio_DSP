// Operators
// https://en.wikipedia.org/wiki/Operators_in_C_and_C%2B%2B
#include <iostream>

int a = 14;
int b = 13;

// Arithmetic
int addition = a + b;
int subtraction = a - b;
int unary_plus = +a;
int unary_minus = -a;
int multiplication = a * b;
int division = a / b;
int modulo = a % b;
int increment_prefix = ++a;
int increment_postfix = a++;

// Comparision
bool equal_to = a == b;
bool not_equal_to = a != b;
//bool bigger_than = (a > b) ? true : false;
bool greater_than = a > b;
bool less_than = a < b;
bool greater_equal = a >= b;
bool less_equal = a <= b;

// Logical
bool negation_a;
bool negation_b;


int main(){
    delete &a;
    // std::boolalpha (True, False)     std::noboolapha (1, 0) 
    std::cout << " -- Operators -- " << std::endl;
    std::cout << "a: " << a << "\t b: " << b << std::endl;
    std::cout << std::endl;

    std::cout << " - Arithmetic - " << std::endl;
    std::cout << "a + b: \t \t" << addition << std::endl;
    std::cout << "a - b: \t \t" << subtraction << std::endl;
    std::cout << "+a: \t \t" << unary_plus << std::endl;
    std::cout << "-a: \t \t" << unary_minus << std::endl;
    std::cout << "a * b: \t \t" << multiplication << std::endl;
    std::cout << "a / b: \t \t" << division << std::endl;
    std::cout << "a % b: \t \t" << modulo << std::endl;
    std::cout << "++a: \t \t" << increment_prefix << std::endl;
    std::cout << "a++: \t \t" << increment_postfix << std::endl;
    std::cout << std::endl;

    std::cout << " - Comparison - " << std::endl;
    std::cout << std::boolalpha << "x == y: \t" << equal_to << std::endl;  
    std::cout << std::boolalpha << "x != y: \t" << not_equal_to << std::endl;   
    std::cout << std::boolalpha << "x > y: \t \t" << greater_than << std::endl;   
    std::cout << std::boolalpha << "x < y \t \t" << less_than << std::endl;                     

}