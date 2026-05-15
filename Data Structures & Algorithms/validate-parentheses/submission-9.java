class Solution {
    public boolean isOpen (char c){
        if ((c == '{')||(c == '[')||(c=='(')){
            return true;
        }
        return false;
    }
    public boolean isValid(String s) {
        if ((s.length() == 0) || (s.length() ==1)){
            return false;
        }
        Stack<Character> stack = new Stack<>();
        Map <Character, Character> compliment = new HashMap <>();
        compliment.put(')','(');
        compliment.put('}','{');
        compliment.put(']','[');
        for (Character c: s.toCharArray()){
            if (isOpen(c)){
                stack.push(c);
                continue;
            }
            if ((stack.isEmpty())||(stack.peek() != compliment.get(c))){
                return false;
            }
            if (stack.peek() == compliment.get(c)){
                stack.pop();
            }
        }
        return stack.isEmpty();
    }
}
