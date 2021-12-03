#include <iostream>
#include <fstream>
using namespace std;

int main() {
	ifstream infile;
	infile.open("aoc01_input.txt");

	int c = 0;
	int last[3] {0, 0, 0};
	int next;
	infile >> last[0];
	infile >> last[1];
	infile >> last[2];
	
	while(infile >> next) {
		if(last[0] < next)
			c++;
		last[0] = last[1];
		last[1] = last[2];
		last[2] = next;
	}
	cout << c;

	return 0;
}