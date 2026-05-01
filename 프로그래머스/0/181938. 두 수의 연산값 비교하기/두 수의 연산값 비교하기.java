class Solution {
    public int solution(int a, int b) {
        int n1 = Integer.parseInt("" + a + b);
        int n2 = 2 * a * b;
    
        return n1 == n2 ? n1 : Math.max(n1, n2);
    }
}