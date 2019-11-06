package string.q294_flipGameII;

class Solution {
    char[] chars;
    public boolean canWin() {
        for (int i = 0; i <= chars.length - 2; i++) {
            if (chars[i] == '+' && chars[i + 1] == '+') {
                chars[i] = chars[i + 1] = '-';
                boolean ifCanWin = canWin();
                chars[i] = chars[i + 1] = '+';
                if (!ifCanWin)
                    return true;
            }
        }
        return false;
    }
    public boolean canWin(String s) {
        chars = s.toCharArray();
        return canWin();
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        //List<String> res = s.generatePossibleNextMoves("++++");
        boolean res = s.canWin("++++");
        System.out.println(res);
    }
}
