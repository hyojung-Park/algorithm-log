import java.util.*;

class Solution {
    public String solution(String s) {
        char[] arr = s.toCharArray();
        Arrays.sort(arr);
        
        String result = new StringBuilder(String.valueOf(arr)).reverse().toString();
        
        return result;
    }
}