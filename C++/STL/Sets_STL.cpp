#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int queries, action, num;
    set<int>s;
    cin >> queries;
    while(queries>0){
        cin >> action >> num;
        switch(action){
            case(1): s.insert(num);
                queries--;
                break;
            case(2): s.erase(num);
                queries--;
                break;
            case(3): set<int>::iterator itr=s.find(num);
                if(itr==s.end()) cout << "No" << endl;
                else cout << "Yes" << endl;
                queries--;
                break;
        }
    }
    return 0;
}
