class Solution {
    public boolean isPalindrome(String s) {
        int leftcount = 0;
        int rightcount = s.length()-1;
        for (int i =0; i<s.length(); i++){
            Character right = s.charAt(rightcount);
            Character left = s.charAt(leftcount);
            right = Character.toLowerCase(right);
            left = Character.toLowerCase(left);
            if (leftcount>=rightcount){
                return true;
            }
            if (!(right >= 48 && right <= 57) && !(right >= 97 && right <= 122)) {
                rightcount--;
                continue;
            }   
            if (!(left >= 48 && left <= 57) && !(left >= 97 && left <= 122)) {
                leftcount++;
                continue;
            }
            if (right!=left){
                return false;
            }
            leftcount++;
            rightcount--;
        }
        return true;
    }
}
