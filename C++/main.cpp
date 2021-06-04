#include <iostream>
#include <vector>

int main(){
    int fs = 48000;
    int t = 3;
    int N = fs * t;

    std::cout << "Abtastfrequenz: \t"<< fs << std::endl;
    std::cout << "Zeit: \t \t \t \t"<<t << std::endl;
    std::cout << "Samples: \t \t \t" << N << std::endl;




    return 0;
}