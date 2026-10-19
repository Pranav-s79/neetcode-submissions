class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> dict1,dict2; //creates 2 maps

        if (s.size() != t.size()) {return false;}

        for (char c:s){
            dict1[c]++; //populates maps
        }
        for (char c:t){
            dict2[c]++; //populates maps
        }

        for (const auto& kv:dict1){
            char key = kv.first;
            int freq = kv.second;

            auto it = dict2.find(key); //returns a pointer to the key pair value
            if(it==dict2.end()|| it->second != freq){
                return false;
            }
        }
        return true;
    }
};
