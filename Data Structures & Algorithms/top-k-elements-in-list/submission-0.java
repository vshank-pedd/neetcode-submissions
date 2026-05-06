class Solution {
    public Integer mostFrequent (int [] nums, Integer completed){
        Map <Integer, Integer> map = new HashMap <>();
        Map <Integer, Integer> inverted = new HashMap <>(); 
        int counter = 0;   
        for (int i =0; i<nums.length; i++){
            if (completed!= null && nums[i] == completed){
                nums[i] = 247483647;
            }
            if (nums[i] == 247483647){
                continue;
            }
            if (map.get(nums[i])==null){
                map.put(nums[i], 1);
            }
            else{
                map.put(nums[i], 1 + map.get(nums[i]));
            }
            if (map.get(nums[i])>counter){
                counter = map.get(nums[i]);
            }
        }
        for (Integer key: map.keySet()){
            if (map.get(key) == counter){
                return key;
            }
        }
        return null;
    }
    public int[] topKFrequent(int[] nums, int k) {
        int [] solution = new int [k];
        int temp = mostFrequent(nums, null);
        solution[0] = temp;
        for (int i =1; i<k; i++){
            temp = mostFrequent(nums, temp);
            solution[i] = temp;
        }
        return solution;
    }
}
