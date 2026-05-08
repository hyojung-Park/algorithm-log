class Solution {
    public int[] solution(int start_num, int end_num) {
        int cnt = end_num - start_num + 1;
        int[] list = new int[cnt];
        int cur = start_num;
        
        for(int i = 0; i < cnt; i++){
            list[i] = cur;
            cur += 1;
        }
        
        return list;
    }
}