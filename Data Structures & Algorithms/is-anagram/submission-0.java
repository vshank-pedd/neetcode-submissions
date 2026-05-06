class Solution {
    public boolean isAnagram(String s, String t) {
        if (t.length()!=s.length()){
            return false;
        }
        char [] s1 = s.toCharArray();
        Arrays.sort(s1);
        char [] t1 = t.toCharArray();
        Arrays.sort(t1);
        if (Arrays.equals(s1,t1) == true){
            return true;
        }
        else{
            return false;
        }
    }
}
