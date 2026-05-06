public class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> solution = new ArrayList<>();
        for (int i = 0; i < nums.length-2; i++) {
            int target = 0-nums[i];
            int r = nums.length-1;
            int l = i+1;
            if (i>0){
                if(nums[i] == nums[i-1]){
                    continue;
                }
            }
            //-4 -1 -1 0 1 2 
            while(r>l){
                List<Integer> triplet = new ArrayList<>();
                if ((nums[l] + nums[r]) == target){
                    triplet.add(0-target);
                    triplet.add(nums[l]);
                    triplet.add(nums[r]);
                    solution.add(triplet);
                    while (l < r && nums[l] == nums[l + 1]) { l++;}
                    while (l < r && nums[l] == nums[r - 1]) { r--;}
                    l++;
                    r--;
                }
                else if ((nums[l] + nums[r])>target){
                    r--;
                }
                else if ((nums[l] + nums[r])<target){
                    l++;
                }
            }
        }
        return solution;
    }
}