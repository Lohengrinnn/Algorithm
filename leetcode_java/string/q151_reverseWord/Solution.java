package string.q151_reverseWord;

class Solution {
    public String reverseWords1(String s) {
        int end_index = s.length() - 1;
        int end_nospace_index = -1;
        StringBuffer sBuffer = new StringBuffer();
        for (int i = end_index; i >= 0; i--) {
            if (s.charAt(i) != ' ' && end_nospace_index == -1) {
                end_nospace_index = i;
            }
            if (s.charAt(i) == ' ' || i == 0) {
                if (end_nospace_index != -1) {
                    if (sBuffer.length() != 0) {
                        sBuffer.append(' ');
                    }
                    if (s.charAt(i) == ' ') {
                        sBuffer.append(s.substring(i + 1, end_nospace_index + 1));
                    } else {
                        sBuffer.append(s.substring(i, end_nospace_index + 1));
                    }
                    end_nospace_index = -1;
                }
            }
        }
        return sBuffer.toString();
    }

    public String reverseWords(String s) {
        String wordArray[] = s.split(" ");
        StringBuilder sbuilder = new StringBuilder();
        for (int i = wordArray.length - 1; i >= 0; i--) {
            if (wordArray[i].length() == 0)
                continue;

            if (sbuilder.length() != 0)
                sbuilder.append(" ");
            sbuilder.append(wordArray[i]);
        }
        return sbuilder.toString();
    }
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.reverseWords(" a hello world!  hellow word a "));
    }
}