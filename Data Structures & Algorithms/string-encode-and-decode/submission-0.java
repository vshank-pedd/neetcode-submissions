class Solution {

    public String encoding(String string){
        String solution = "";
        for (int i = 0; i<string.length();i++){
            int num  = 1 + (int) string.charAt(i);
            String temp = String.valueOf((char)num);
            solution = solution + temp;
        }
        return solution;
    }

    public String encode(List<String> strs) {
        String solution = "";
        int count = 0;
        for (int i = 0; i<strs.size(); i++){
            solution = solution + encoding(strs.get(i));
            solution = solution + " ";
            count++;
        }
        solution = String.valueOf((char) count) + solution;
        return solution;

    }

    public List<String> decode(String str) {
        int num = (int) str.charAt(0);
        List<String> strs = new ArrayList <>(num);
        String temp = "";
        for (int i = 1; i<str.length();i++){
            if (str.charAt(i) == ' '){
                strs.add(temp);
                temp = "";
                continue;
            }
            int number = ((int)str.charAt(i)) -1;
            temp = temp+ String.valueOf((char)number);
        }
        return strs;
    }
}
