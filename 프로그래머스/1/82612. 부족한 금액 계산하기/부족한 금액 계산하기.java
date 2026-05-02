class Solution {
    public long solution(int price, int money, int count) {
        long fee = 0;
        for (int i = 1; i < count + 1; i++){
            fee += i * price;
        }
        long ans = money - fee;
        
        return ans < 0 ? -ans : 0;
    }
}