class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        StringBuilder sb = new StringBuilder();
        char [] myArr = my_string.toCharArray();
        char [] overArr = overwrite_string.toCharArray();
        
        for (int i = 0; i < s; i++){
            sb.append(myArr[i]);
        }
        
        for (int i = 0; i < overwrite_string.length(); i++){
            sb.append(overArr[i]);
        }
        
        for (int i = s + overwrite_string.length(); i < my_string.length(); i++){
            sb.append(myArr[i]);
        }
        
        return sb.toString();
    }
}