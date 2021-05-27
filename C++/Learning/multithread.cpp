#include <iostream>
#include <thread>                                       // https://en.cppreference.com/w/cpp/thread/thread
#include <chrono>

void printNumbers(int max, std::string name){
    std::cout << name;
    for (int i = 0; i<max; ++i){
         std::cout <<  i << " ";   
    }
    std::cout << std::endl;
}
    


int main(){
    std::thread numberThread(printNumbers,5,"Thread 1: ");                  // Class: Thread
    numberThread.join();
    printNumbers(5,"Thread 2: ");
} 