#include <iostream>
#include <fstream>
using namespace std;

int main() {
    ifstream infile;
    infile.open("aoc02_input.txt");

    int x = 0;
    int y = 0;
    string d;
    int s;
    
    while(infile >> d) {
        infile >> s;

        if(d[0] == 'f') {
            x += s;
        } else if(d[0] == 'u') {
            y -= s;
        } else if(d[0] == 'd') {
            y += s;
        }
    }
    cout << x * y;

    return 0;
}