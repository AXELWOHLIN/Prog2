#include <cstdlib>
// Person class 

class Person{
	public:
		Person(int);
		int get();
		void set(int);
		int fib();
		int fib2(int);
	private:

		int age;
		int fib2(int);
Person::Person(int n){
	age = n;
}
int Person::fib(){

	if(age<=1){
		return age;
			}
	else{
	     	return (this->fib2(age-1) + this->fib2(age-2) );
		}
}

int Person::get(){
	return age;
	}
int Person::fib2(int n){
	if(n<=1){
                return n;
                        }
        else{
                return (fib2(n-1) + fib2(n-2) );
                }
	}
void Person::set(int n){
	age = n;
	}


extern "C"{
	Person* Person_new(int n) {return new Person(n);}
	int Person_get(Person* person) {return person->get();}
	int Person_fib(Person* person) {return person->fib();}
	void Person_set(Person* person, int n) {person->set(n);}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	}
