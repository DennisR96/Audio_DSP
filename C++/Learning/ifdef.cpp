// ifDef

#include <iostream>

#define Var

int main(){
    #ifdef Var                          // ifdef: Wenn {Var} definiert, dann {x}
    std::cout << "Definiert!";
    #endif

    #ifndef Var                         // ifndef: Wenn {Var} nicht definiert, dann {x}
    std::cout << "Nicht definiert!";
    #endif

}