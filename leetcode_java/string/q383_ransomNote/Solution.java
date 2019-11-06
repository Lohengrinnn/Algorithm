package string.q383_ransomNote;

import java.util.HashMap;

class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        HashMap<Character, Integer> letterCount = new HashMap<Character, Integer>();
        char[] chars = ransomNote.toCharArray();
        for (int i = 0, n = chars.length; i < n; i++) {
            letterCount.put(chars[i], letterCount.getOrDefault(chars[i], 0) + 1);
        }
        char[] magazine_chars = magazine.toCharArray();
        for (int i = 0, n = magazine_chars.length; i < n; i++) {
            Integer num = letterCount.getOrDefault(magazine_chars[i], 0);
            if (num > 1) {
                letterCount.put(magazine_chars[i], num - 1);
            } else if (num == 1) {
                letterCount.remove(magazine_chars[i]);
            }
        }
        return letterCount.isEmpty();
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.canConstruct("aba", "aaa"));
        System.out.println(s.canConstruct("aba", "baa"));
    }
}