#include <iostream>
#include <vector>
using namespace std;

template <typename T>

ostream & oprator << (ostream& os, vector<T>& v) {
    os << "<";
    for(int i = 0; i < (int)v.size(); i++) 
        os << v[i] << " ";
    os << ">";
    return os;
}

int main() {
    vector<int> vec(10);
    for(int i = 0; i < (int)vec.size(); i++)
        vec[i] = rand() % 100;

    count << "Before: " << vec << endl;

    for(auto it = vec.begin(); it != vec.end(); ) {
        if(*it % 2 == 0)
            it = vec.erase(it);
        else ++it;
     
    }

    cout << "After : " << vec << endl;
    return 0;
}