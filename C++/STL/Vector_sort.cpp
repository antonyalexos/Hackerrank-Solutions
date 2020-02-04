#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int size=0;
    vector<int>v;
    int num;
    cin >> size;
    for(int i=0;i<size;i++){
        cin >> num;
        v.push_back(num);
    }
    sort(v.begin(),v.end());
    for(int i=0;i<size;i++){
        cout << v[i] << " ";
    }
    return 0;
}
