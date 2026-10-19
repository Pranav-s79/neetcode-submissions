#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> seen; //initializes hash set
        for(int num:nums){
            if (seen.count(num)){
                return true;
            }
            seen.insert(num);
        }
        return false;
    }
};