package string.q186_reverse_string2;

public class Solution {
    public void reverseWords1(char[] s) {
        for (int i = 0; i < s.length / 2; i++) {
            char tmp = s[i];
            s[i] = s[s.length - 1 - i];
            s[s.length - 1 - i] = tmp;
        }

        int i = 0;
        while (i < s.length) {
            int e = i;
            while (e < s.length && s[e] != ' ') {
                e++;
            }
            for (int j = i; j < (i + e) / 2; j++) {
                char tmp = s[j];
                s[j] = s[e - 1 - j + i];
                s[e - 1 - j + i] = tmp;
            }
            i = e + 1;
        }
    }

    private void reverseWord(char[] s, int l, int r)
    {
        while (l < r) {
            char tmp = s[l];
            s[l] = s[r];
            s[r] = tmp;
            l++;
            r--;
        }
    }

    public void reverseWords(char[] s) {
        this.reverseWord(s,0, s.length - 1);
        int i = 0;
        while (i < s.length) {
            int e = i;
            while (e < s.length && s[e] != ' ') {
                e++;
            }
            this.reverseWord(s, i, e - 1);
            i = e + 1;
        }
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        char[] ca = "all hello world world! hellow all".toCharArray();
        //char[] ca = "all".toCharArray();
        s.reverseWords(ca);
        System.out.println(ca);
    }
}
