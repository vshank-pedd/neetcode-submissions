class Solution {
    public int longestConsecutive(int[] nums) {
        Map <Integer, Integer> map = new HashMap<>();
        Map <Integer, Integer> reverse_map = new HashMap<>();
        Map <Integer,Integer> duplicate_check = new HashMap<>();
        for (int i = 0; i<nums.length; i++){
            if (duplicate_check.containsKey(nums[i])){
                continue;
            }
            duplicate_check.put(nums[i],i);
            int upperbound = nums[i] + 1;
            int lowerbound = nums[i] - 1;
            // [3, 20, 0,1,2, 4, 5 ] [0,1,2,3,4,5,20]
            // [1:2] --> after hitting 2 on bottom []
            // [2:1] --> after hitting 2 on bottom [], remove 2:1
            if (reverse_map.containsKey(nums[i]) && reverse_map.containsValue(nums[i])){
                int temp_val = reverse_map.get(nums[i]); //used for deleting and setting this as lower bound
                map.remove(temp_val);
                reverse_map.remove(nums[i]);
                int second_val = map.get(nums[i]); //upper bound
                reverse_map.remove(second_val);
                map.remove(nums[i]);
                map.put(temp_val,second_val);
                reverse_map.put(second_val, temp_val);
                continue;
            }
            if (reverse_map.containsKey(nums[i])){ //altering maps, if reversemap was a hit
                int temp_val = reverse_map.get(nums[i]); //key for regular map
                reverse_map.remove(nums[i]);
                reverse_map.put(nums[i]+1, temp_val);
                map.put(temp_val, nums[i]+1);
                continue;
            }
            if (map.containsKey(nums[i])){
                int temp_val = map.get(nums[i]); // key for reversehash
                map.remove(nums[i]);
                map.put(nums[i]-1, temp_val);
                reverse_map.put(temp_val, nums[i]-1);
                continue;
            }
            reverse_map.put(upperbound,lowerbound);
            map.put(lowerbound, upperbound);
        }
        Set<Integer> keys = map.keySet();
        int solution = 0;
        int length = 0;
        for (Integer key:keys){
            length = map.get(key) - key -1;
            if (length>solution){
                solution = length;
            }
            System.out.println(key);
        }
        return solution;
        
    }
}
