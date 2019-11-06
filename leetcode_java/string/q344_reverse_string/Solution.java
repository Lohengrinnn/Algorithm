package string.q344_reverse_string;


class Solution {
    public void reverseString(char[] s) {
        int n = Math.round((s.length - 2) / 2);
        for (int i = 0; i <= n; i++) {
            char tmp = s[i];
            s[i] = s[s.length - 1 - i];
            s[s.length - 1 - i] = tmp;
        }
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        //char[] chars = {'h', 'e', 'i', 'l', 'o', 'H'};
        char[] chars = {'h', 'i'};
        s.reverseString(chars);
        System.out.println(chars);
    }
}