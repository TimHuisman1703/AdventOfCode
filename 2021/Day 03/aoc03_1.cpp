#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main() {
    ifstream infile;
    infile.open("aoc03_input.txt");

    vector<string> l = {};
    
    string d;
    while(infile >> d) {
        l.push_back(d);
    }

    int n = l[0].size();

    int g = 0;
    int e = 0;
    
    for(int i = 0; i < n; i++) {
        int ones = 0;
        int zeros = 0;

        for(string j : l) {
            if(j[i] == '0')
                zeros++;
            else
                ones++;
        }

        g <<= 1;
        e <<= 1;

        if(ones >= zeros)
            g |= 1;
        else
            e |= 1;
    }
    
    cout << g * e;

    return 0;
}