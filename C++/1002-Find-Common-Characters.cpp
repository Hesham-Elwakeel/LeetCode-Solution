Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.

class Solution {
 public:
  vector<string> commonChars(vector<string>& words) {
    vector<string> ans;
    vector<int> commonCount(26, INT_MAX);

    for (const string& word : words) {
      vector<int> count(26);
      for (const char c : word)
        ++count[c - 'a'];
      for (int i = 0; i < 26; ++i)
        commonCount[i] = min(commonCount[i], count[i]);
    }

    for (char c = 'a'; c <= 'z'; ++c)
      for (int i = 0; i < commonCount[c - 'a']; ++i)
        ans.push_back(string(1, c));

    return ans;
  }
};
