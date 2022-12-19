#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main() {
    ifstream infile;
    infile.open("aoc03_input.txt");

    vector<string> l {};
    
    string d;
    while(infile >> d) {
        l.push_back(d);
    }
    
    int n = l[0].size();

    vector<string> s = l;
    int a = 0;
    for(int i = 0; i < n; i++) {
        int ones = 0;
        int zeros = 0;

        for(string j : s) {
            if(j[i] == '0')
                zeros++;
            else
                ones++;
        }

        a <<= 1;
        if(ones >= zeros)
            a |= 1;
        
        vector<string> ns {};
        for(string j : s) {
            if((int) (j[i] - 0x30) == (int) (a & 1)) {
                ns.push_back(j);
            }
        }
        
        s = ns;
    }

    s = l;
    int b = 0;
    for(int i = 0; i < n; i++) {
        int ones = 0;
        int zeros = 0;

        if(s.size() == 1) {
            b <<= 1;
            b |= s[0][i] - 0x30;
            continue;
        }

        for(string j : s) {
            if(j[i] == '0')
                zeros++;
            else
                ones++;
        }

        b <<= 1;
        if(ones < zeros)
            b |= 1;
        
        vector<string> ns {};
        for(string j : s) {
            if((int) (j[i] - 0x30) == (int) (b & 1)) {
                ns.push_back(j);
            }
        }
        
        s = ns;
    }

    cout << a * b;

    return 0;
}