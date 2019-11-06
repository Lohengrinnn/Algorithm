package string.q205_isIsomorphic;

import java.util.HashMap;

public class Solution {
    public boolean isIsomorphic(String s, String t) {
        if (s.length() != t.length())
            return false;
        HashMap<Character, Character> map = new HashMap<Character, Character>();
        HashMap<Character, Character> rmap = new HashMap<Character, Character>();
        for (int i = 0; i < s.length(); i++) {
            if (map.keySet().contains(s.charAt(i))) {
                if (map.get(s.charAt(i)) != t.charAt(i))
                    return false;
            } else {
                if (rmap.keySet().contains(t.charAt(i)))
                    return false;
                map.put(s.charAt(i), t.charAt(i));
                rmap.put(t.charAt(i), s.charAt(i));
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.isIsomorphic("paper", "title"));
    }

}
