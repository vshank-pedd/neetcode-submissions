class Solution {
    public boolean isAnagram(String s, String t) {
        if (t.length()!=s.length()){
            return false;
        }
        Map <Character, Integer> map = new HashMap <>();
        Map <Character, Integer> secondmap = new HashMap <>();
        for (int i = 0; i<s.length(); i++){
            if (map.get(s.charAt(i))!=null){
                map.put(s.charAt(i), 1 + map.get(s.charAt(i)));
            }
            else{
                map.put(s.charAt(i),1);
            }
            if (secondmap.get(t.charAt(i))!=null){
                secondmap.put(t.charAt(i), 1 + secondmap.get(t.charAt(i)));
            }
            else{
                secondmap.put(t.charAt(i),1);
            }
        }
        for (int j = 0; j<s.length(); j++){
            if (!map.get(s.charAt(j)).equals(secondmap.get(s.charAt(j)))){
                return false;
            }
        }
        return true;
    }
}