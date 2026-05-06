class Solution {
    public boolean isAnagram(String one, String two){
    if (one.length()!=two.length()){
        return false;
    }
    Map <Character, Integer> map = new HashMap <>();
    Map <Character, Integer> secondmap = new HashMap <>();
    for (int i = 0; i<one.length();i++){
        if (map.get(one.charAt(i))!= null){
            map.put(one.charAt(i),1+map.get(one.charAt(i)));
        }
        else{
            map.put(one.charAt(i),1);
        }
        if (secondmap.get(two.charAt(i))!= null){
            secondmap.put(two.charAt(i),1+secondmap.get(two.charAt(i)));
        }
        else{
            secondmap.put(two.charAt(i),1);
        }
    }
    for (int j = 0; j<one.length();j++){
        if (!map.get(one.charAt(j)).equals(secondmap.get(one.charAt(j)))){
            return false;
        }
    }
    return true;
}

    public List<List<String>> groupAnagrams(String[] strs) {
        List <List<String>> solution = new ArrayList<> ();  // List<String> → List<List<String>>
        for (int i = 0; i<strs.length; i++){  // str → strs
            if (!strs[i].equals("1234567890QWERTYUIASDFGHJXCVBNSDFGHERTYU")){  // str → strs
                List <String> group = new ArrayList<>();
                for (int j = 0; j<strs.length; j++){  // str → strs
                    if (isAnagram(strs[i],strs[j])){  // str → strs
                        group.add(strs[j]);  // str → strs
                        System.out.println(strs[i]+" " + strs[j]);
                        if (j!=i){
                            strs[j] = "1234567890QWERTYUIASDFGHJXCVBNSDFGHERTYU";  // str → strs
                        }
                    }
                }
                solution.add(group);
            }
        }
        return solution;
    }
}