#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int queries, action, marks;
    string name;
    map<string,int>m;
    cin >> queries;
    while(queries>0){
        cin >> action >> name;
        switch(action){
            case(1): cin >> marks;
                m[name] += marks;
                queries--;
                break;
            case(2): m[name] = 0;
                queries--;
                break;
            case(3):
                cout << m[name] << endl;
                queries--;
                break;
        }
    }
    return 0;
}
