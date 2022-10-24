class Solution { // 36 ms, faster than 66.95%
public:
    int maxLength(vector<string>& arr) {
        int n = arr.size(), allMask = 1 << n, ans = 0;
        for (int mask = 0; mask < allMask; ++mask) {
            int strSize = 0;
            int seen = 0; // the mask to check duplicate chars when forming string
            bool isValid = true;
            for (int i = 0; i < n; ++i) {
                if (((mask >> i) & 1) == 0) continue;
                for (char c : arr[i]) {
                    int j = c - 'a';
                    if ((seen >> j) & 1) { // If c is already existed then it's invalid subsequence.
                        isValid = false;
                        break;
                    }
                    seen = seen | (1 << j); // mark as character `c` is already seen
                    strSize += 1;
                }
                if (!isValid) break; //  prune when there is a duplicate
            }
            if (isValid && strSize > ans) ans = strSize;
        }
        return ans;
    }
};