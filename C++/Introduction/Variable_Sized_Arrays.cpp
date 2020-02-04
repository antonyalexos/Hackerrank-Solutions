#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n,q,place,size,querry;
    cin >> n >> q;
    int **array = new int*[n]();
    for(int i=0;i<n;i++){
        cin >> size;
        int *arr = new int[size]();
        for(int j=0;j<size;j++){
            cin >> arr[j];
        }
        array[i] = arr;
    }
    for(int i=0;i<q;i++){
        cin >> querry >> place;
        cout << array[querry][place] << endl;
    }
    for(int j=0;j<size;j++){
        delete[] array[j];
    }
    return 0;
}
