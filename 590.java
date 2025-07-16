/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
}
*/

class Solution {
    public List<Integer> postorder(Node root) {
        // time: O(n), space: O(n)
        List<Integer> result = new ArrayList<>();
        if (root == null) return result;
        Stack<NodeVisitPair> nodeStack = new Stack<>();
        nodeStack.push(new NodeVisitPair(root, false));
        while (!nodeStack.isEmpty()) {
            NodeVisitPair currentPair = nodeStack.pop();
            if (currentPair.isVisited) {
                result.add(currentPair.node.val);
            } else {
                currentPair.isVisited = true;
                nodeStack.push(currentPair);
                List<Node> children = currentPair.node.children;
                for (int i = children.size() - 1; i >= 0; i--) {
                    nodeStack.push(new NodeVisitPair(children.get(i), false));
                }
            }
        }
        return result;
    }

    private class NodeVisitPair {
        Node node;
        boolean isVisited;
        NodeVisitPair(Node node, boolean isVisited) {
            this.node = node;
            this.isVisited = isVisited;
        }
    }
}