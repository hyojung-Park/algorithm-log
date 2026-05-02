class Solution {
    public int[] solution(int[] num_list) {
        // 마지막 원소가 > 이전 원소, 마지막 원소 - 이전 원소
        // 마지막 원소 < 그 전 원소 , 마지막 원소 * 2
        
        int len = num_list.length;
        int [] arr = new int[len + 1];
        
        for ( int i = 0; i < len; i++){
            arr[i] = num_list[i];
        }
        
        if (num_list[len-1] > num_list[len-2]){
            arr[len] = num_list[len-1] - num_list[len-2];
        } else {
            arr[len] = num_list[len-1] * 2;
        }
    
        return arr;
    }
}