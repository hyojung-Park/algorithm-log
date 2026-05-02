class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        
        for(int [] q : queries){
            int temp = 0;
            temp = arr[q[1]];
            arr[q[1]] = arr[q[0]];
            arr[q[0]] = temp;
        }
        
        return arr;
    }
}