class Solution {
    public int solution(int n) {
        int ans1 = 0;
        int ans2 = 0;
        for (int i = 0; i <= n; i++){
            if (i % 2 == 0){
                ans2 += i * i;
            } else {
                ans1 += i;
            }
        }
            
        return n % 2 == 0 ? ans2 : ans1;
    }
}