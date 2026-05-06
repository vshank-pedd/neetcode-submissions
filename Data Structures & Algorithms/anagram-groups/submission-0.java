class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Integer> countS = new HashMap<>();
        HashMap<Character, Integer> countT = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            countS.put(s.charAt(i), countS.getOrDefault(s.charAt(i), 0) + 1);
            countT.put(t.charAt(i), countT.getOrDefault(t.charAt(i), 0) + 1);
        }
        return countS.equals(countT);
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