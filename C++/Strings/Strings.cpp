#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    // Complete the program
    string a;
    string b;
    
    cin >> a >> b;
    cout << a.size() << " " << b.size() << endl;
    cout << a+b << endl;
    swap(a[0],b[0]);
    cout << a << " " << b;
    
    return 0;
}
