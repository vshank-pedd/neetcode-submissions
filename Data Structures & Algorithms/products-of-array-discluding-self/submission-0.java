class Solution {
    public int recursion (int[]nums, int index, int value){
        if (index>nums.length-1){
            return 1;
        }
        if (index == value){
            return 1 *  recursion(nums, 1 + index,  value);
        }
        return nums[index] * recursion (nums, 1 + index,  value);

    }
    public int[] productExceptSelf(int[] nums) {
        int [] solution = new int [nums.length];
        for (int i =0; i<nums.length;i++){
            solution[i] = recursion(nums, 0, i);
        }
        return solution;
    }
}  
