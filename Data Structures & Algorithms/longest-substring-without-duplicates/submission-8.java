class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map <Character, Integer> check = new HashMap <> ();
        int max = 0;
        int l =0;
        for (int i =0; i<s.length();i++){
            if (check.get(s.charAt(i))==null){
                check.put(s.charAt(i),i);
            }
            else{
                l = Math.max(check.get(s.charAt(i)) + 1, l);
            }
            max=Math.max(max,1+i-l);
            check.put(s.charAt(i),i);
        }
        return max;
    }
}
