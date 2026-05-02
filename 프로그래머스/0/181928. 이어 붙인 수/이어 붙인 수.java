class Solution {
    public int solution(int[] num_list) {
        String odd = "";
        String even = "";
        
        for (int n : num_list){
            if (n % 2 == 0){
                odd += n + "";
            } else {
                even += n + "";
            }
        }
            
        return Integer.parseInt(odd) + Integer.parseInt(even);
    }
}