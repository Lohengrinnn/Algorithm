package graph.q133_cloneGraph;

import java.util.*;

class Node {
    public int val;
    public List<Node> neighbors;

    public Node() {}

    public Node(int _val, List<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};

class Solution {
    public Node cloneGraph(Node node) {
        HashMap<Node, Node> nodeMap = new HashMap<Node, Node>();
        Queue<Node> srcNode = new LinkedList<Node>();

        srcNode.offer(node);
        Node head = new Node(node.val, new ArrayList<Node>());
        nodeMap.put(node, head);
        while (!srcNode.isEmpty()) {
            Node n = srcNode.poll();
            Node cn = nodeMap.get(n);
            for (Node nn: n.neighbors) {
                if (nodeMap.containsKey(nn)) {
                    cn.neighbors.add(nodeMap.get(nn));
                } else {
                    Node cnn = new Node(nn.val, new ArrayList<Node>());
                    cn.neighbors.add(cnn);
                    nodeMap.put(nn, cnn);
                    srcNode.add(nn);
                }
            }
        }
        return head;
    }


    private void printNode(Node node, List<Node> expanded) {
        System.out.printf("%d, {", node.val);
        if (!expanded.contains(node)) {
            expanded.add(node);
            System.out.printf("\n");
            for (Node n: node.neighbors) {
                printNode(n, expanded);
            }
        }
        System.out.printf("} \n");
    }
    private void printGraph(Node node) {
        List<Node> expanded = new ArrayList<Node>();
        printNode(node, expanded);
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        Node n1 = new Node(1, new ArrayList<Node>());
        Node n2 = new Node(2, new ArrayList<Node>());
        Node n3 = new Node(3, new ArrayList<Node>());
        Node n4 = new Node(4, new ArrayList<Node>());
        n1.neighbors.add(n2);
        n1.neighbors.add(n4);
        n2.neighbors.add(n1);
        n2.neighbors.add(n3);
        n3.neighbors.add(n2);
        n3.neighbors.add(n4);
        n4.neighbors.add(n3);
        n4.neighbors.add(n1);
        s.printGraph(n1);
        Node nc = s.cloneGraph(n1);
        s.printGraph(nc);
    }
}
