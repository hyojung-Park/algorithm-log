class Solution {
    public String solution(int[] numLog) {
        StringBuilder sb = new StringBuilder();
        StringBuilder ans = new StringBuilder();
        
        for(int i = numLog.length - 1; i >= 1; i--){
            int cal = numLog[i] - numLog[i-1];
            
            switch (cal){
                case 1: sb.append("w"); break;
                case -1: sb.append("s"); break;
                case 10: sb.append("d"); break;
                case -10: sb.append("a"); break;
            }
        }
        
        char [] str = sb.toString().toCharArray();
        
        for (int i = sb.length()-1; i >= 0; i--){
            ans.append(str[i]);
        }
        
        return ans.toString();
    }
}