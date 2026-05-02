class Solution {
    public String solution(String code) {
        String answer = "";
        int mode = 0;
        char [] arr = code.toCharArray();
        
        for (int i = 0; i < code.length(); i++){
            if (mode == 0){
                if (arr[i] != '1'){
                    if (i % 2 == 0){
                        answer += arr[i];
                    }
                } else {
                    mode = 1;
                }
            } else {
                if (arr[i] != '1'){
                    if (i % 2 != 0){
                        answer += arr[i];
                    }
                } else {
                    mode = 0;
                }
            }
        }
        
        return answer.length() != 0 ? answer : "EMPTY";
    }
}