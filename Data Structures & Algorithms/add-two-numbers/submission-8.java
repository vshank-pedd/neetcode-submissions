/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode first_curr = l1;
        ListNode second_curr = l2;
        ListNode Solution = new ListNode ();
        ListNode iter = Solution;
        int counter = 0;
        while (first_curr!=null || second_curr!=null){
            int first = 0;
            int second = 0;
            if(first_curr != null){
                first = first_curr.val;
            }
            if (second_curr != null){
                second = second_curr.val;
            }
            int answer = first+ second + counter;
            if (answer>=10){
                answer = answer%10;
                counter =1;
            }
            else{
                counter =0;
            }
            iter.next = new ListNode(answer);
            iter = iter.next;
            if (first_curr!=null){
                first_curr = first_curr.next;
            }
            if (second_curr!=null){
                second_curr= second_curr.next;
            }
        }
        if (counter == 1){
            iter.next = new ListNode(1);
        }
        return Solution.next;
    }
}