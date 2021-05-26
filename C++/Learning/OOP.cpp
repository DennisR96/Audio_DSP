#include <iostream>
class Cars{
    public: 
    void set_year( int v ); 
    int  get_year( void );

    private:
    // Zugriff nur durch durch andere Member

    int year;
};

void Cars::set_year(int v){
        year = v;
    }

int Cars::get_year( void ){
        return year;
    }

int main(){
    Cars *Toyota = new Cars(); 
    Toyota->set_year(2002);
    std::cout << "Der Wagen wurde " <<Toyota->get_year() << " hergestellt" << std::endl;
    delete Toyota;

    return 0;
    
}