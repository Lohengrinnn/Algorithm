package string.q345_reverseVowels;

public class Solution {
    public String reverseVowels(String s) {
        int l = 0, r = s.length() - 1;
        char[] clist = s.toCharArray();
        String vowels = "aeiouAEIOU";
        while (l < r) {
            if (vowels.indexOf(clist[l]) < 0) {
                l++;
                continue;
            }
            if (vowels.indexOf(clist[r]) < 0) {
                r--;
                continue;
            }
            char tmp = clist[l];
            clist[l] = clist[r];
            clist[r] = tmp;
            l++;
            r--;
        }
        return String.valueOf(clist);
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.reverseVowels("leetcode"));
    }
}
