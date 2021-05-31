/*
Pointers:
Variable that holds a memory adress

(&)Adress           (*)Value                        Code                            Bedeutung
100 ["c"]           5                               int c = *b;                     c ist gleich dem Wert von Adresse b
101
102 ["a"]           5                               int a = 5;                      a ist gleich 5
103
104 ["b"]           102                             int* b = &a;                    b ist ein int Pointer zu Adresse a

*/ 

#include <iostream>

void array_pointer(){
    int array[5] = {9,8,7,6,5};
    std::cout << " " << std::endl;
    std::cout <<"-- Adress and Value of an array -- " << std::endl;

    for (int i = 0; i < sizeof(array)/sizeof(*array); i++){
    std::cout << "Adress: " << &array[i] <<  " Value: " << array[i] << std::endl;
        //std::cout << array[i] << std::endl;;
    }
}

int main(){
    int a = 5;
    int* b = &a;
    int c = *b;
    std::cout << "Value a: " << a <<std::endl;
    std::cout << "Pointer b: " << b <<std::endl;
    std::cout << "Value c: " << c << std::endl;

    array_pointer();
}