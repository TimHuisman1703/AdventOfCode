#include <iostream>
#include <fstream>
using namespace std;

int main() {
	ifstream infile;
	infile.open("aoc01_input.txt");

	int c = 0;
	int last, next;
	infile >> last;
	
	while(infile >> next) {
		if(last < next)
			c++;
		last = next;
	}
	cout << c;

	return 0;
}