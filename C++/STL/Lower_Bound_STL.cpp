#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    vector<int>v;
    int size, num, queries;
    vector<int>::iterator low;
    cin >> size;
    for(int i=0;i<size;i++){
        cin >> num;
        v.push_back(num);
    }
    cin >> queries;
    while(queries>0){
        cin >> num;
        low = lower_bound(v.begin(), v.end(), num);
        if (v[low - v.begin()] == num) cout << "Yes " << (low - v.begin()+1) << endl;
        else cout << "No " << (low - v.begin()+1) << endl;
        queries--;
    }
    return 0;
}
