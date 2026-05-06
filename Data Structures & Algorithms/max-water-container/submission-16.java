class Solution {
    //I need to check everything
    //hash set
    // 1 2 3 4 5 6 7 8 
    // 0 1 2 3 4 5 6 7
    // 1 7 2 5 4 7 3 6
    // delta
    public int maxArea(int[] heights) {
        /*
        int sol = 0;
        int left_ptr = heights[0];
        int leftidx = 0;
        for (int i = 0; i<heights.length; i++){
            if ((heights[i] - left_ptr) >= (i - leftidx)){
                left_ptr = heights[i];
                leftidx = i;
                for (int j = leftidx+1; j<heights.length; j++){
                    int min = Math.min(left_ptr, heights[j]);
                    int area = (min*(j-leftidx));
                    sol = Math.max(area,sol);
                }
            }
        }
        return sol;
        */
        int sol = 0;
        int l = 0;
        int r = heights.length - 1;
        int min;
        while(r>l){
            min  = Math.min(heights[r], heights[l]);
            sol = Math.max(sol,min*(r-l));
            if (heights[r]>heights[l]){
                l++;
            }
            else{
                r--;
            }
        }
        return sol;
    }
}