// Loops
#include <iostream>


void for_loop(){
    std::cout << "For Loop:\t";
    for (int i=0; i<10; i++){
        std::cout << i << "\t";
    }
}

void case_switch(int x){
    switch(x){
        case 0:
            std::cout << "Switch_Case 0:\t x ist 0 ";
            break;
        case 1:
            std::cout << "Switch_Case 1:\t x ist 1";
            break;
        case 2:
            std::cout << "Switch_Case 2:\t x ist 2";
            break;
        case 3:
            std::cout << "Switch_Case 3:\t x ist 3";
            break;
    }
}



int main(){
    case_switch(3);

}