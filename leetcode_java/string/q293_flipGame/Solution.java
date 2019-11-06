package string.q293_flipGame;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.List;

public class Solution {
    public List<String> generatePossibleNextMoves(String s) {
        List<String> res = new ArrayList<String>();
        char[] chars = s.toCharArray();
        int i = 0;
        while (i < chars.length - 1) {
            int ti = s.indexOf("++", i);
            if (ti < 0)
                break;
            chars[ti] = chars[ti + 1] = '-';
            res.add(String.valueOf(chars));
            chars[ti] = chars[ti + 1] = '+';
            i = ti + 1;
        }
        return res;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        //List<String> res = s.generatePossibleNextMoves("++++");
        List<String> res = s.generatePossibleNextMoves("--");
        System.out.println(res);
    }
}
