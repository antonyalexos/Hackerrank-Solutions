#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int size, num, number;
    vector<int>v;
    cin >> size;
    while(size>0){
        cin >> num;
        v.push_back(num);
        size--;
    }
    cin >> num;
    v.erase(v.begin()+num-1);
    cin >> num >> number;
    v.erase(v.begin()+num-1,v.begin()+number-1);
    cout << v.size() << endl;
    for(int i=0;i<v.size();i++){
        cout << v[i] << " ";
    }
    return 0;
}
