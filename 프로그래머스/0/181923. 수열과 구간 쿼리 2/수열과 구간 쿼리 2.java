class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] ans = new int[queries.length];
        
        for(int i = 0; i < queries.length; i++){
            int s = queries[i][0];
            int e = queries[i][1];
            int k = queries[i][2];
            
            int minNum = 1000000;
            for (int j = s; j <= e; j++){
                if (arr[j] > k && arr[j] < minNum){
                    minNum = arr[j];
                }
            }
            
            if(minNum == 1000000){
                ans[i] = -1;
            } else{
                ans[i] = minNum;
            }

        }
        
        return ans;
    }
}