class Solution {
    public int maxProfit(int[] prices) {
        if (prices==null || prices.length==1){
            return 0;
        }
        int left = 0;
        int right =1;
        int max = prices[right]-prices[left];
        for (int i = 0; i<prices.length; i++){
            if (prices[left]>prices[right]){
                left = right;
            }
            right++;
            if (right==(prices.length)){
                right--;
            }
            int temp = prices[right]-prices[left];
            if (max<(temp)){
                max = temp;
            }
        }
        return (max);
    }
}