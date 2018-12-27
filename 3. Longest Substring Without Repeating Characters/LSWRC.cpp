#include "LSWRC.h"
#include <iostream>

using namespace std;

Solution::lengthOfLongestSubstring(string s){
    
    int table [52], length = {0}, 0;
    
    for(int i=0, i< s.length(); ++i)
    {
        if ((s[i]-'A') < 25){
            cout<<"III"<<endl;
        }
        else{
            cout<<"ABC"<<endl;
        }
    }

    return length;
}
