class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int left = 0;
        int right = numbers.length-1;
        for (int i =0;i<numbers.length;i++){
            if (numbers[left]+numbers[right]==target){
                return new int [] {1+left,1+right};
            }
            if (numbers[left]+numbers[right]>target){
                right--;
            }
            if (numbers[left]+numbers[right]<target){
                left++;
            }
        }
        return new int [] {numbers[left],numbers[right]};
    }
}
