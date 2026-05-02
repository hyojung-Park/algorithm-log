import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        int[] temp = new int[arr.length];
        int idx = 0;
        
        temp[idx++] = arr[0];
        
        for(int i=1; i< arr.length; i++){
            if (arr[i] != arr[i-1]){
                temp[idx++] = arr[i];
            }
        }
        
        int[] result = new int[idx];
        for (int i = 0; i < idx; i++){
            result[i] = temp[i];
        }
        
        return result;
    }
}