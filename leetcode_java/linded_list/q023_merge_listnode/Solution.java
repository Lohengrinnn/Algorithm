package linded_list.q023_merge_listnode;

import java.util.Comparator;
import java.util.PriorityQueue;

class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}

class Solution {
    private ListNode mergeTwoLists(ListNode a, ListNode b) {
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;
        while (a != null && b != null) {
            if (a.val < b.val) {
                cur.next = a;
                a = a.next;
            } else {
                cur.next = b;
                b = b.next;
            }
            cur = cur.next;
        }
        if (a == null) {
            cur.next = b;
        } else {
            cur.next = a;
        }
        return dummy.next;
    }
    public ListNode mergeKLists1(ListNode[] lists) {
        if (lists.length == 0)
            return null;
        ListNode res = lists[0];
        for (int i = 1; i < lists.length; i++) {
            res = this.mergeTwoLists(res, lists[i]);
        }
        return res;
    }

    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> pq = new PriorityQueue<ListNode>(new Comparator<ListNode>() {
            @Override public int compare(ListNode listNode, ListNode t1) {
                return listNode.val - t1.val;
            }
        });

        for (ListNode ln: lists) {
            if (ln != null)
                pq.add(ln);
        }
        ListNode head = new ListNode(0);
        ListNode tail = head;
        while (pq.size() != 0) {
            tail.next = pq.poll();
            tail = tail.next;
            if (tail.next != null)
                pq.add(tail.next);
        }
        return head.next;
    }
    public static void main(String[] args) {
        Solution s = new Solution();
        /*ListNode[] ln = {new ListNode(1), new ListNode(1), new ListNode(2)};
        ln[0].next = new ListNode(4);
        ln[0].next.next = new ListNode(5);
        ln[1].next = new ListNode(3);
        ln[1].next.next = new ListNode(4);
        ln[2].next = new ListNode(6);*/
        ListNode[] ln = {null};
        ListNode ln_m = s.mergeKLists(ln);
        while (ln_m != null) {
            System.out.println(ln_m.val);
            ln_m = ln_m.next;
        }
    }
}