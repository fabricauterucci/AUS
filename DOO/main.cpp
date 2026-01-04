// main.cpp
#include "cache.h"
#include <iostream>
#include <cstring>


class Student{
	int id;
	int value;
	const char* data;
public:
	static const string class_name; // Cada clase tiene un static llamado: class_name
	// Constructor por defecto
    Student() : id(0), value(0), data("") {}
	Student(int _key, int _value, const char* _data): id(_key), value(_value), data(_data){
	}
	~Student(){};
	const char* getData() const {
        return data;
    }
	
	void print() const{
		cout<<"Studen Object: "<<id<<", "<<value<<", "<<data<<endl;
	}
    
     friend std::ostream& operator<<(std::ostream& os, const Student& student) {
        os << student.id << ' ' << student.value << ' ' << (student.data ? student.data : "");
        return os;
    }

    friend std::istream& operator>>(std::istream& is, Student& student) {
        is >> student.id >> student.value;
        char buffer[256];
        is.getline(buffer, 256);
        student.data = strdup(buffer); // Necesita liberar memoria en el destructor
        return is;
    }
};

const string Student::class_name = "StudentClass";
//////////////////////////////////////////////////
/////////////////////////////////////////////////////
int main(){
	CacheManager<Student> my_cache(3);
	
	my_cache.insert("0", Student(0, 22, "student1"));
	my_cache.insert("1", Student(1, 23, "student2"));
	my_cache.insert("2", Student(2, 25, "student3"));
	my_cache.insert("3", Student(3, 29, "student4"));
	
	my_cache.show_cache();
	
	cout<<"   --------------------------- UPDATE ------------------------------- " << endl;
	my_cache.insert("2", Student(22,222,"EZE"));
	my_cache.show_cache();
	
	cout << "   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< " << endl;
	Student return_obj = my_cache.get("0"); //no en la cache pero si en los archivos del sistema
	cout << "   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< " << endl;
	my_cache.insert("2", Student(2,25,"EZE"));
	my_cache.show_cache();
	
	my_cache.insert("9", Student(1, 5, "Nine"));
	my_cache.insert("9", Student(1, 5, "Nine"));
	my_cache.insert("9", Student(1, 5, "Nine"));
	my_cache.show_cache();
	
	return 0;
}

// Codigo de main.cpp y cache.h Hecho por Fabrizio Cauterucci, con la teoria vista de clases
