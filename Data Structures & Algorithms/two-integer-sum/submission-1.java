class Solution {
    public int[] twoSum(int[] nums, int target) {
        int [] solution = new int[2];
        Map <Integer, Integer> map = new HashMap <>();
        for (int i =0; i<nums.length; i++){
            if (map.get(nums[i])!=null){
                solution [1] = i;
                solution [0] = map.get(nums[i]);
                return solution;
            }
            map.put(target-nums[i],i);
        }
        return solution;
    }
}
