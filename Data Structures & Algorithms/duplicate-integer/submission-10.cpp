#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        for (int n = 0; n<nums.size(); n++){
            for (int i = n+1; i<nums.size();i++){
                if (nums[n] == nums[i]){
                    return true;
                }
            }

        }
        return false;
    }
};